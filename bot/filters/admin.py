from aiogram.filters import BaseFilter
from aiogram.types import Message

from bot.data.config import config


class ForAdmins(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        if config.admin == message.from_user.id:
            return True
