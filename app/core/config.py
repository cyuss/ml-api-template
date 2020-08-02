# -*- coding: utf-8 -*-

from starlette.config import Config
from starlette.datastructures import Secret


APP_VERSION = "0.1.0"
APP_NAME = "Machine Learning project template"
APP_DESCRIPTION = ""
API_PREFIX = "/api"
API_LOGGER_NAME = "base_logger"

# no autoload .env file by poetry
config = Config(".env")

DEFAULT_MODEL_PATH: str = config("DEFAULT_MODEL_PATH", cast=str, default="")