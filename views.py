from fastapi import APIRouter, HTTPException
from services import UserService, FavoriteService, AssetService
from schemas import (
    UserCreateInput,
    Standard,
    ErrorOutput,
    UserFavoriteAddInput,
    UserListOutput,
    DaySummaryOutpuy,
)
from typing import List
import asyncio

user_router = APIRouter(prefix="/user")
assets_router = APIRouter(prefix="/assets")


@user_router.post("/", response_model=Standard, responses={400: {"model": ErrorOutput}})
async def create_user(user_input: UserCreateInput):
    try:
        await UserService.create(name=user_input.name)
        return Standard(message="OK")
    except Exception as e:
        raise HTTPException(400, detail=str(e))


@user_router.delete(
    "/{pk}", response_model=Standard, responses={400: {"model": ErrorOutput}}
)
async def delete_user(pk: int):
    try:
        await UserService.delete(pk=pk)
        return Standard(message="OK")
    except Exception as e:
        raise HTTPException(400, detail=str(e))


@user_router.get(
    "/", response_model=List[UserListOutput], responses={400: {"model": ErrorOutput}}
)
async def list_user():
    try:
        await UserService.list()
        return Standard(message="OK")
    except Exception as e:
        raise HTTPException(400, detail=str(e))


@user_router.post(
    "/favorite/", response_model=Standard, responses={400: {"model": ErrorOutput}}
)
async def create_favorite_user(favorite: UserFavoriteAddInput):
    try:
        await FavoriteService.add(user_id=favorite.user_id, symbol=favorite.symbol)
        return Standard(message="OK")
    except Exception as e:
        raise HTTPException(400, detail=str(e))


@user_router.delete(
    "/favorite/{user_id}",
    response_model=Standard,
    responses={400: {"model": ErrorOutput}},
)
async def delete_favorite_user(user_id: int, symbol: str):
    try:
        await FavoriteService.remove(user_id=user_id, symbol=symbol)
        return Standard(message="OK")
    except Exception as e:
        raise HTTPException(400, detail=str(e))


# @assets_router.get("/day_summary/{symbol}", response_model=DaySummaryOutpuy , responses={400: {"model": ErrorOutput}})
# async def day_summary(symbol: str):
#     try:
#         result = await AssetService.day_summary(symbol=symbol)
#         return DaySummaryOutpuy(**result)
#     except Exception as e:
#         raise HTTPException(400, detail=str(e))


@assets_router.get(
    "/day_summary/{user_id}",
    response_model=List[DaySummaryOutpuy],
    responses={400: {"model": ErrorOutput}},
)
async def day_summary(user_id: int):
    try:
        user = await UserService.by_id(pk=user_id)
        favorite_symbols = [favorite.symbol for favorite in user.favorites]
        tasks = [AssetService.day_summary(symbol=symbol) for symbol in favorite_symbols]
        result = await asyncio.gather(*tasks)
        return result
    except Exception as e:
        raise HTTPException(400, detail=str(e))
