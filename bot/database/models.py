from sqlalchemy import BigInteger, func
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

from .db import Base


class Users(Base):
    __tablename__ = "users"

    user_id: Mapped[int] = mapped_column(BigInteger, primary_key=True, nullable=False)
    first_name: Mapped[str] = mapped_column(nullable=False)
    registration: Mapped[datetime] = mapped_column(server_default=func.now(), nullable=False)
