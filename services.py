from db.postgres import models
from db.postgres.connection import async_session
from sqlalchemy import delete
from sqlalchemy.future import select
from aiohttp import ClientSession
from datetime import datetime, timedelta


class UserService:
    async def create(name: str):
        async with async_session() as session:
            user = models.User(name=name)
            session.add(user)
            await session.commit()

    async def delete(pk: int):
        async with async_session() as session:
            await session.execute(delete(models.User).where(models.User.id == pk))
            await session.commit()

    async def list():
        async with async_session() as session:
            data = await session.execute(select(models.User))
            return data.scalars().all()

    async def by_id(pk: int):
        async with async_session() as session:
            data = await session.execute(
                select(models.User).where(models.User.id == pk)
            )
            return data.scalar()


class FavoriteService:
    async def add(user_id: int, symbol: str):
        async with async_session() as session:
            favorite = models.Favorite(user_id=user_id, symbol=symbol)
            session.add(favorite)
            await session.commit()

    async def remove(user_id: int, symbol: str):
        async with async_session() as session:
            await session.execute(
                delete(models.Favorite).where(
                    models.Favorite.user_id == user_id, models.Favorite.symbol == symbol
                )
            )
            await session.commit()


class AssetService:
    async def day_summary(symbol: str):
        async with ClientSession() as session:
            headers = {"Accept": "application/json"}
            yesterday = datetime.now() - timedelta(days=1)
            BASE_URL = "https://www.mercadobitcoin.net/api/"
            url = f"{BASE_URL}{symbol}/day-summary/{yesterday.year}/{yesterday.month}/{yesterday.day}/"
            response = await session.get(url=url, headers=headers)
            data = await response.json()
            data = {
                "highest": data["highest"],
                "lowest": data["lowest"],
                "symbol": symbol,
            }
            return data
