from aiogram.fsm.state import StatesGroup, State


class EncryptionKeyInput(StatesGroup):
    working_with_cipher = State()


class Hash_input(StatesGroup):
    get_text_for_hash = State()
