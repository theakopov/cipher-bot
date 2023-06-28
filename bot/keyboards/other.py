from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from .callback_data import Back_data, Ciphers_data


def get_cipher_page(cipher: str) -> InlineKeyboardMarkup:
    b = InlineKeyboardBuilder()
    b.row(
        InlineKeyboardButton(
            text="About",
            callback_data=Ciphers_data(cipher=cipher, action="about").pack(),
        )
    )
    b.row(
        InlineKeyboardButton(
            text="Encrypt",
            callback_data=Ciphers_data(cipher=cipher, action="encrypt").pack(),
        ),
        InlineKeyboardButton(
            text="Decrypt",
            callback_data=Ciphers_data(cipher=cipher, action="decrypt").pack(),
        ),
    )
    b.row(
        InlineKeyboardButton(
            text="<--", callback_data=Back_data(cipher=cipher, lvl="ciphers").pack()
        )
    )
    return b.as_markup()


def get_back_button(cipher: str, lvl: str) -> InlineKeyboardMarkup:
    b = InlineKeyboardBuilder()
    b.add(
        InlineKeyboardButton(
            text="<--", callback_data=Back_data(cipher=cipher, lvl=lvl).pack()
        )
    )
    return b.as_markup()


def get_try_again_button(cipher: str) -> InlineKeyboardMarkup:
    b = InlineKeyboardBuilder()
    b.add(InlineKeyboardButton(text="Try again", callback_data="try_again"))
    b.add(
        InlineKeyboardButton(
            text="Back to menu",
            callback_data=Back_data(cipher=cipher, lvl="ciphers").pack(),
        )
    )
    return b.as_markup()
