from aiogram import Router
from aiogram.filters import Command, StateFilter
from aiogram.filters.text import Text
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from ...keyboards import (
    get_ciphers_buttons,
    get_hash_buttons,
    get_menu_buttons,
    get_cipher_page,
    Back_data,
)
from ...data.texts.main import help_text
from ...database import Repository

router = Router()


@router.message(StateFilter("*"), Command(commands=["start", "cancel"]))
async def start(message: Message, repo: Repository, state: FSMContext):
    await state.clear()

    await repo.create_user(message.from_user.id, message.from_user.first_name)
    await message.answer("Menu", reply_markup=get_menu_buttons())


@router.message(StateFilter("*"), Command("help"))
async def help(message: Message, state: FSMContext):
    await state.clear()

    await message.answer(help_text, disable_web_page_preview=True)


@router.callback_query(StateFilter("*"), Text(("encrypt", "back_ciphers")))
async def get_ciphers(callback: CallbackQuery):
    await callback.message.edit_text(
        "Choose a cipher", reply_markup=get_ciphers_buttons()
    )


@router.callback_query(StateFilter("*"), Text(("hash", "back_ciphers")))
async def get_ciphers(callback: CallbackQuery):
    await callback.message.edit_text(
        "Choose a hash", reply_markup=get_hash_buttons()
    )


@router.callback_query(StateFilter("*"), Back_data.filter())
async def back(callback: CallbackQuery, state: FSMContext, callback_data: Back_data):
    """Handler for moving to a certain level in bot navigation"""
    await state.clear()

    match callback_data.lvl:
        case "start":
            await callback.message.edit_text("Menu", reply_markup=get_menu_buttons())

        case "cipher":
            await callback.message.edit_text(
                f"""Cipher: <code>{callback_data.cipher} cipher</code>""",
                reply_markup=get_cipher_page(callback_data.cipher),
            )

        case "ciphers":
            await callback.message.edit_text(
                "Choose an encryption method", reply_markup=get_ciphers_buttons()
            )
        case "hash":
            await callback.message.edit_text("Choose a hash", reply_markup=get_hash_buttons())
