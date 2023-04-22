from fastapi import APIRouter, HTTPException
from services import UserService
from schemas import UserCreateInput, Standard, ErrorOutput

user_router = APIRouter(prefix="/user")
assets_router = APIRouter(prefix="/assets") 
  
@user_router.post("/create", response_model=Standard, responses={400: {"model": ErrorOutput}})
async def create_user(user_input: UserCreateInput):
    try: 
        await UserService.create(name=user_input.name)
        return Standard(message="OK")
    except Exception as e:
        raise HTTPException(400, detail=str(e))

@user_router.delete("/delete/{pk}", response_model=Standard, responses={400: {"model": ErrorOutput}})
async def delete_user(pk: int):
    try: 
        await UserService.delete(pk=pk)
        return Standard(message="OK")
    except Exception as e:
        raise HTTPException(400, detail=str(e))