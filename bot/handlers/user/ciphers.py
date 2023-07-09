from os import getenv
from logging import basicConfig

from aiogram import Router, Bot
from aiogram.exceptions import TelegramBadRequest
from aiogram.filters import StateFilter
from aiogram.filters.text import Text
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext

from ...filters import CheckKey, DefaultEncryption
from ...models import EncryptionKeyInput
from ...data.texts.about import description_ciphers
from ...data.texts.key_description import description_ciphers_keys
from ...data.config import config
from ...misc import Cipher
from ...keyboards import (
    get_cipher_page,
    get_back_button,
    get_try_again_button,
    Ciphers_data,
)

router = Router()


@router.callback_query(Text(list(Cipher.CIPHERS.values())))
async def show_cipher(callback: CallbackQuery, state: FSMContext, logger: basicConfig):
    await state.clear()

    await callback.message.edit_text(
        f"""Cipher: <code>{callback.data} cipher</code>""",
        reply_markup=get_cipher_page(callback.data),
    )
    logger.info(
        f"{callback.data.title()} has been requested by {callback.from_user.id}")


@router.callback_query(Ciphers_data.filter())
async def cryptographer(
    callback: CallbackQuery, callback_data: Ciphers_data, state: FSMContext
):
    action = callback_data.action
    cipher = callback_data.cipher

    match action:
        case "about":
            await callback.message.edit_text(
                text=description_ciphers.get(cipher),
                reply_markup=get_back_button(cipher=cipher, lvl="cipher"),
            )
        case "encrypt" | "decrypt":
            await state.set_state(EncryptionKeyInput.working_with_cipher)
            await state.set_data(
                {
                    "cipher": cipher,
                    "message_id": callback.message.message_id,
                    "action": action,
                }
            )
            await callback.message.edit_text(
                f"""Enter Key\n\n{description_ciphers_keys.get(cipher)}""",
                reply_markup=get_back_button(cipher=cipher, lvl="cipher")
            )


@router.callback_query(Text("try_again"))
async def try_again(callback: CallbackQuery, state: FSMContext):
    data: dict = await state.get_data()

    await callback.message.delete()
    msg = await callback.message.answer("Enter text to encrypt")
    data["message_id"] = msg.message_id
    await state.set_data(data)


@router.message(StateFilter(EncryptionKeyInput.working_with_cipher))
async def encrpyt_message(message: Message, state: FSMContext, bot: Bot):
    data = await state.get_data()

    cipher = data.get("cipher")
    action = data.get("action")
    key = data.get("key")
    message_id = int(data.get("message_id"))

    await message.delete()

    try:
        await bot.delete_message(
            chat_id=message.from_user.id,
            message_id=message_id,
        )
    except TelegramBadRequest:
        pass

    if key is None and getattr(CheckKey, cipher)(message.text):
        msg = await message.answer(f"Enter text to {action}")
        data["key"] = message.text
    elif key is not None and len(message.text) < 4000:
        result = getattr(Cipher, cipher)(
            message.text, key, action=action
        )

        text = (
            f"""<b>Cipher:</b> <code>{cipher} cipher</code>\n"""
            f"""<b>Action:</b> <code>{action}\n</code>"""
            f"""<b>Key</b>: <code>{key}\n\n</code>"""
            f"""<b>Result:</b> <code>{result}</code>"""
        )

        try:
            msg = await message.answer(
                text, reply_markup=get_try_again_button(cipher)
            )
        except TelegramBadRequest:
            msg = await message.answer(
                "It seems your message is too long.\n Use /cancel  or try again"
            )
    elif data.get("key") is None:
        msg = await message.answer(
            f"""An error was made while entering the key."""
            f"""Use /cancel  or try again\n\n"""
            f"""{description_ciphers_keys.get(cipher)}"""
        )
    else:
        msg = await message.answer(
            "It seems your message is too long.\n Use /cancel  or try again"
        )
    data["message_id"] = msg.message_id
    await state.set_data(data)


@router.message(DefaultEncryption())
async def default_encrypt(message: Message, encrypt: bool, logger: basicConfig):
    await message.delete()
    if encrypt is True:
        result = "0x" + \
            (Cipher.aes(message.text, config.key.get_secret_value(), "encrypt"))
    else:
        result = Cipher.aes(
            message.text[2:], config.key.get_secret_value(), "decrypt")

    try:
        tmp = "\n" if encrypt is True else ""
        text = (
            f"""<b>Cipher:</b> <code>Default (AES)</code>\n"""
            f"""<b>Action:</b> <code>{"encrypt" if encrypt is True else "decrypt"}\n</code>"""
            f"""{"<b>Key:</b>  <code>To decrypt the cipher, it must be sent to the bot </code>" + tmp}\n"""
            f"""<b>Result:</b> <code>{result}</code>"""
        )
        await message.answer(text)
    except TelegramBadRequest:
        await message.answer(
            "It seems your message is too long.\n Use /cancel  or try again"
        )

    logger.info(f"{message.from_user.id} used default cipher")
