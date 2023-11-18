from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base


Base = declarative_base()
metadata = Base.metadata


def create_db(url: str):
    """Creates an engine and session to the database

    Args:
        url (str): a DSN string for a database connection

    Returns:
        Repository: class for working with database
    """    
    from .requests import Repository

    engine = create_async_engine(url, future=True)
    conn = async_sessionmaker(bind=engine)
    return Repository(conn, engine)
