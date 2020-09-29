# -*- coding: utf-8 -*-

from typing import Callable

from fastapi import FastAPI
from loguru import logger

from app.core import settings
from app.core import setup_logger


def start_app_handler(app: FastAPI) -> Callable:
    def startup() -> None:
        setup_logger.setup_logging()
        logger.info("Service initialization")

    return startup


def stop_app_handler(app: FastAPI) -> Callable:
    def shutdown() -> None:
        logger.info("Preparing the service shutdown.")

    return shutdown