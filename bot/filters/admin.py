from aiogram.filters import BaseFilter
from aiogram.types import Message

from ..data.config import config


class ForAdmins(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        return config.admin == message.from_user.id
