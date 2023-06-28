from sqlalchemy import Column, Text, BigInteger, Date, func
from .db import Base


class Users(Base):
    __tablename__ = "users"

    user_id = Column(BigInteger, primary_key=True, nullable=False)
    first_name = Column(Text, nullable=False)
    registration = Column(Date, default=func.now())
