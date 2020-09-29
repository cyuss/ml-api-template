# -*- coding: utf-8 -*-

import time
from contextvars import ContextVar
from loguru import logger
from uuid import uuid4

from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request


CORRELATION_ID_CTX_KEY = 'correlation_id'
REQUEST_ID_CTX_KEY = 'request_id'

_correlation_id_ctx_var: ContextVar[str] = ContextVar(CORRELATION_ID_CTX_KEY, default=None)
_request_id_ctx_var: ContextVar[str] = ContextVar(REQUEST_ID_CTX_KEY, default=None)


def get_correlation_id() -> str:
    return _correlation_id_ctx_var.get()


def get_request_id() -> str:
    return _request_id_ctx_var.get()


class RequestContextLogMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint):
        correlation_id = _correlation_id_ctx_var.set(request.headers.get('X-Correlation-ID', str(uuid4())))
        request_id = _request_id_ctx_var.set(str(uuid4()))
        # update the request ID into the logger
        logger.configure(extra={"request_id": get_request_id()})
        # time the main request's function
        start_time = time.time()
        response = await call_next(request)
        process_time = time.time() - start_time
        # create response headers
        response.headers['X-Process-Time'] = str(process_time)
        response.headers['X-Correlation-ID'] = get_correlation_id()
        response.headers['X-Request-ID'] = get_request_id()
        logger.info("Process time: {:.5f}s".format(process_time))
        # reset the starlette context
        _correlation_id_ctx_var.reset(correlation_id)
        _request_id_ctx_var.reset(request_id)

        return response