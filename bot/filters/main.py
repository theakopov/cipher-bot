from aiogram.filters import BaseFilter
from aiogram.types import Message


class DefaultEncryption(BaseFilter):
    """
    Default encryption filter.
    Specifies whether to encrypt or decrypt the input.
    """

    async def __call__(self, message: Message) -> bool:
        if message.text[:2] != "0x":
            d = {"encrypt": True}
        else:
            d = {"encrypt": False}

        return d
