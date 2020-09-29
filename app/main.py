# -*- coding: utf-8 -*-

from fastapi import FastAPI
from loguru import logger

from app.core import settings
from app.core.event_handlers import start_app_handler, stop_app_handler
from app.core.middlewares import RequestContextLogMiddleware
from app.routes import api_router


def get_app() -> FastAPI:
	logger.info("App Initialization")
	fast_app = FastAPI(title=settings.APP_NAME, version=settings.APP_VERSION)
	fast_app.include_router(api_router, prefix=settings.API_PREFIX)
	fast_app.add_event_handler("startup", start_app_handler(fast_app))
	fast_app.add_event_handler("shutdown", stop_app_handler(fast_app))
	fast_app.add_middleware(RequestContextLogMiddleware)

	return fast_app

app = get_app()