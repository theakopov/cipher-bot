from aiogram import BaseMiddleware
from aiogram.types import Message, TelegramObject, Update

from typing import Union, Callable, Dict, Awaitable, Any, Optional

from ..database import Cache


class AntiFloodMiddleware(BaseMiddleware):
    """
    Middleware for anti-flood messages from users

    The bot ignores messages from the user if he
    wrote a message before the end of the time limit,
    which is set in .env.
    """

    def __init__(self, limit: Union[float, int]):
        self.cache = Cache(limit)

    async def __call__(self,
                       handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
                       event: TelegramObject,
                       data: Dict[str, Any]
                       ) -> Optional[Any]:
        user = data.get("event_from_user")
        update: Update = data.get("event_update")
        if user is not None:
            if self.cache.check_user(user.id):
                return await update.message.answer("Too many requests")
            self.cache.add_user(user.id)
        return await handler(event, data)
