from os import getenv
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

DATABASE = getenv("DATABASE")

engine = create_async_engine(DATABASE)
async_session = sessionmaker(engine, class_=AsyncSession)