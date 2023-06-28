from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.ext.asyncio import AsyncSession


Base = declarative_base()
metadata = Base.metadata


def create_db(url: str):
    "Creates an engine and session to the database"
    from .requests import Repository

    engine = create_async_engine(url, future=True)
    conn = sessionmaker(bind=engine, class_=AsyncSession,
                        expire_on_commit=False)
    return Repository(conn, engine)
