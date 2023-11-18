import hashlib
from logging import basicConfig

from aiogram import Router, Bot
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext
from aiogram.filters import Text, StateFilter
from aiogram.exceptions import TelegramBadRequest

from ...models import Hash_input
from ...keyboards import get_back_button

hashes = ('md5', 'sha1',
          'sha256', 'sha512',
          'blake2b', 'blake2s')

router = Router()


@router.callback_query(Text(text=hashes), StateFilter("*"))
async def hash_input(callback: CallbackQuery, state: FSMContext, logger: basicConfig):
    """Getting a hash from a user"""    
    await state.set_state(Hash_input.get_text_for_hash)

    msg = await callback.message.edit_text(text=f"Hash: <code>{callback.data}</code>\n\nEnter text to hash",
                                           reply_markup=get_back_button(lvl="hash", cipher=""),
                                           disable_notification=True)
    await state.set_data({"message_id": msg.message_id, "hash": callback.data})
    logger.info(
        f"{callback.data.title()} has been requested by {callback.from_user.id}")


@router.message(StateFilter(Hash_input.get_text_for_hash))
async def hashing(message: Message, state: FSMContext, bot: Bot):
    """Hashing data"""
    data = await state.get_data()

    await message.delete()
    try:
        await bot.delete_message(chat_id=message.from_user.id, message_id=int(data.get("message_id")))
    except TelegramBadRequest:
        pass

    if len(message.text) > 4000:
        msg = await message.answer(
            "It seems your message is too long.\n Use /cancel  or try again"
        )
        data["message_id"] = msg.message_id
        await state.set_data(data)
    else:
        await state.clear()
        result = getattr(hashlib, data.get("hash"))(
            message.text.encode("utf-8")).hexdigest()
        await message.answer(f"""Hash: <code>{data.get("hash")}</code>\n\n Result: <code>{result}</code>""",
                             reply_markup=get_back_button(lvl="hash", cipher=""))
