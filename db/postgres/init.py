import asyncio

from db.postgres.connection import engine
from db.postgres.models import Base

async def create_database():
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.drop_all)
        await connection.run_sync(Base.metadata.create_all)
        
if __name__ == '__main__':
    asyncio.run(create_database())
