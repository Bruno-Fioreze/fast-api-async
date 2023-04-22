from fastapi import FastAPI, APIRouter
from views import user_router, assets_router

app = FastAPI()

router = APIRouter()

@router.get("/") 
async def read_root():
    return {"message": "Hello World"}

app.include_router(prefix="/first", router=router)
app.include_router(user_router)
app.include_router(assets_router)
