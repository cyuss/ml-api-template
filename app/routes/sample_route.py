# -*- coding: utf-8 -*-

from fastapi import APIRouter
from starlette.requests import Request

router = APIRouter()

@router.get("/hello", tags=["users"])
async def hello():
    return {"message": "hello world"}