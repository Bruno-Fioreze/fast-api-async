from db.postgres import models
from db.postgres.connection import async_session

class UserService:
    async def create(name):
        async with async_session() as session:
            user = models.User(name=name)
            session.add(user)
            await session.commit()