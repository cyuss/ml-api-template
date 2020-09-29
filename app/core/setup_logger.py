# -*- coding: utf-8 -*-

import sys
import logging
from loguru import logger

from .middlewares import get_request_id, get_correlation_id


def setup_logging() -> None:
    loguru_format = "<green>[{time:YYYY-MM-DD HH:mm:ss.SSS}]</green> - [{extra[request_id]}] - <level>{level: <8}</level> - <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>"
    config = {
        "handlers": [
            {"sink": sys.stderr, "format": loguru_format}
        ],
        "extra": {
            "request_id": get_request_id()
        }
    }
    logger.configure(**config)
