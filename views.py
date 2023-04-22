from fastapi import APIRouter, HTTPException
from services import UserService, FavoriteService
from schemas import UserCreateInput, Standard, ErrorOutput, UserFavoriteAddInput, UserListOutput
from typing import List

user_router = APIRouter(prefix="/user")
assets_router = APIRouter(prefix="/assets") 
  
@user_router.post("/", response_model=Standard, responses={400: {"model": ErrorOutput}})
async def create_user(user_input: UserCreateInput):
    try: 
        await UserService.create(name=user_input.name)
        return Standard(message="OK")
    except Exception as e:
        raise HTTPException(400, detail=str(e))

@user_router.delete("/{pk}", response_model=Standard, responses={400: {"model": ErrorOutput}})
async def delete_user(pk: int):
    try: 
        await UserService.delete(pk=pk)
        return Standard(message="OK")
    except Exception as e:
        raise HTTPException(400, detail=str(e))

@user_router.get("/", response_model=List[UserListOutput], responses={400: {"model": ErrorOutput}})
async def list_user():
    try: 
        await UserService.list()
        return Standard(message="OK")
    except Exception as e:
        raise HTTPException(400, detail=str(e))

@user_router.post("/favorite/", response_model=Standard, responses={400: {"model": ErrorOutput}})
async def create_favorite_user(favorite: UserFavoriteAddInput):
    try: 
        await FavoriteService.add(user_id=favorite.user_id, symbol=favorite.symbol)
        return Standard(message="OK")
    except Exception as e:
        raise HTTPException(400, detail=str(e))
    
@user_router.delete("/favorite/{user_id}", response_model=Standard, responses={400: {"model": ErrorOutput}})
async def delete_favorite_user(user_id: int, symbol: str):
    try: 
        await FavoriteService.remove(user_id=user_id, symbol=symbol)
        return Standard(message="OK")
    except Exception as e:
        raise HTTPException(400, detail=str(e))

