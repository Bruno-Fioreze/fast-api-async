from fastapi import FastAPI, APIRouter

app = FastAPI()

router = APIRouter()

@router.get("/") 
async def read_root():
    return {"message": "Hello World"}

app.include_router(prefix="/first", router=router)
