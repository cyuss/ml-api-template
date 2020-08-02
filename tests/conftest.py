# -*- coding: utf-8 -*-

import pytest

from starlette.config import environ
from starlette.testclient import TestClient

from app.main import get_app


@pytest.fixture()
def test_client():
    app = get_app()
    with TestClient(app) as test_client:
        yield test_client