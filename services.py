from db.postgres import models
from db.postgres.connection import async_session
from sqlalchemy import delete

class UserService:
    async def create(name: str):
        async with async_session() as session:
            user = models.User(name=name)
            session.add(user)
            await session.commit()
            
    async def delete(pk: int):
        async with async_session() as session:
            await session.execute(delete(models.User).where(models.User.id==pk))
            await session.commit()
            

class FavoriteService:
    async def add_favorite(user_id: int, symbol: str):
        async with async_session() as session:
            favorite = models.Favorite(user_id=user_id, symbol=symbol)
            session.add(favorite)
            await session.commit()