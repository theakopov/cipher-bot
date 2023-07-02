from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from .callback_data import Back_data
from ..misc.ciphers import Cipher


def get_menu_buttons() -> InlineKeyboardMarkup:
    b = InlineKeyboardBuilder()

    b.row(InlineKeyboardButton(text="ㅤEncryptㅤ", callback_data="encrypt"))
    b.row(InlineKeyboardButton(text="ㅤHashㅤ", callback_data="hash"))

    return b.as_markup()


def get_ciphers_buttons() -> InlineKeyboardMarkup:
    b = InlineKeyboardBuilder()
    for name, callback in Cipher.CIPHERS.items():
        b.row(InlineKeyboardButton(text=name, callback_data=callback), width=2)
    b.adjust(2)
    b.row(
        InlineKeyboardButton(
            text="<--", callback_data=Back_data(lvl="start", cipher="").pack()
        )
    )
    return b.as_markup()


def get_hash_buttons():
    hashes = ("md5", "sha1", "sha256", "sha512", "blake2b", "blake2s")

    b = InlineKeyboardBuilder()
    for hash in hashes:
        b.row(InlineKeyboardButton(text=hash, callback_data=hash))
    b.adjust(2)

    b.row(
        InlineKeyboardButton(
            text="<--", callback_data=Back_data(lvl="start", cipher="").pack()
        )
    )
    return b.as_markup()
