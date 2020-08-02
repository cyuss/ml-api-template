# -*- coding: utf-8 -*-

from fastapi import APIRouter
from starlette.requests import Request

router = APIRouter()

@router.get("/users/", tags=["users"])
async def read_users():
    return [{"username": "Foo"}, {"username": "Bar"}]