# -*- coding: utf-8 -*-

from starlette.config import Config


APP_VERSION = "0.1.0"
APP_NAME = "Machine Learning project template"
APP_DESCRIPTION = ""
API_PREFIX = "/api"

# no autoload .env file by poetry
config = Config(".env")