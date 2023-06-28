from aiogram.filters.callback_data import CallbackData


class Ciphers_data(CallbackData, prefix="cipher"):
    cipher: str
    action: str


class Back_data(CallbackData, prefix="back"):
    lvl: str
    cipher: str
