from typing import Optional

from sqlalchemy.orm import sessionmaker
from sqlalchemy import select, func
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.asyncio import AsyncEngine

from .models import Users


class Repository:

    def __init__(self, conn: sessionmaker, engine: AsyncEngine) -> None:
        self.conn = conn
        self.engine = engine

    async def create_user(self, user_id: Optional[int], first_name: Optional[str]) -> None:
        """
        Create new user

        :param usser_id: telegram user_id
        :param first_name: telegram first_name
        """
        async with self.conn.begin() as session:
            query = insert(Users).values(
                user_id=user_id, first_name=first_name, registration=func.now()
            )
            await session.execute(query.on_conflict_do_nothing())
            await session.commit()

    async def get_stat(self) -> int:
        """
        Returns the number of users in the bot
        """
        async with self.conn.begin() as session:
            query = select(Users.user_id)
            result = await session.execute(query)
            return len(result.all())
