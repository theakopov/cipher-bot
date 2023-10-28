from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.asyncio import AsyncSession


Base = declarative_base()
metadata = Base.metadata


def create_db(url: str):
    "Creates an engine and session to the database"
    from .requests import Repository

    engine = create_async_engine(url, future=True)
    conn = async_sessionmaker(bind=engine)
    return Repository(conn, engine)
