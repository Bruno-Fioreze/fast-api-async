from db.postgres import models
from db.postgres.connection import async_session
from sqlalchemy import delete

class UserService:
    async def create(name):
        async with async_session() as session:
            user = models.User(name=name)
            session.add(user)
            await session.commit()
            
    async def delete(pk):
        async with async_session() as session:
            await session.execute(delete(models.User).where(models.User.id==pk))
            await session.commit()
            