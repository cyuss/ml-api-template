# -*- coding: utf-8 -*-

import subprocess

from app.core import settings


def test_version(test_client):
	proc = subprocess.Popen(['poetry', 'version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	out, err = proc.communicate()
	out = out.decode("utf-8").rstrip()
	poetry_version = out.split(' ')[1]

	assert settings.APP_VERSION == poetry_version