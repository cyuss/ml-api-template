# -*- coding: utf-8 -*-

from fastapi import FastAPI
from loguru import logger

from app.core import config
from app.routes import api_router


def get_app() -> FastAPI:
	logger.info("App Initialization")
	fast_app = FastAPI(title=config.APP_NAME, version=config.APP_VERSION)
	fast_app.include_router(api_router, prefix=config.API_PREFIX)
	
	return fast_app

app = get_app()