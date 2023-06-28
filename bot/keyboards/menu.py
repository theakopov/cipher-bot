from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from .callback_data import Back_data


def get_menu_buttons() -> InlineKeyboardMarkup:
    b = InlineKeyboardBuilder()
    b.row(InlineKeyboardButton(text="ㅤEncryptㅤ", callback_data="encrypt"))
    b.row(InlineKeyboardButton(text="ㅤHashㅤ", callback_data="hash"))
    return b.as_markup()


def get_ciphers_buttons() -> InlineKeyboardMarkup:
    b = InlineKeyboardBuilder()
    b.row(
        InlineKeyboardButton(text="Caesar cipher", callback_data="caesar"),
        InlineKeyboardButton(text="Vigenere cipher", callback_data="vigenere"),
    )
    b.row(
        InlineKeyboardButton(text="Atbash cipher", callback_data="atbash"),
        InlineKeyboardButton(text="AES", callback_data="aes"),
    )
    b.row(
        InlineKeyboardButton(
            text="<--", callback_data=Back_data(lvl="start", cipher="").pack()
        )
    )
    return b.as_markup()


def get_hash_buttons():
    b = InlineKeyboardBuilder()
    b.row(InlineKeyboardButton(text="md5", callback_data="md5"),
          InlineKeyboardButton(text="sha1", callback_data="sha1"))

    b.row(InlineKeyboardButton(text="sha256", callback_data="sha256"),
          InlineKeyboardButton(text="sha512", callback_data="sha512"))

    b.row(InlineKeyboardButton(text="blake2b", callback_data="blake2b"),
          InlineKeyboardButton(text="blake2s", callback_data="blake2s"))

    b.row(
        InlineKeyboardButton(
            text="<--", callback_data=Back_data(lvl="start", cipher="").pack()
        )
    )
    return b.as_markup()
