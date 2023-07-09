from aiogram import Bot, Dispatcher, F
from aiogram.fsm.storage.memory import MemoryStorage

from .data.config import create_logs, config, _url
from .misc import set_commands
from .database.db import create_db
from .handlers import base, ciphers, hash, main
from .middlewares import AntiFloodMiddleware


async def start_bot():
    # init DataBase
    repo = create_db(_url)
        # f"postgresql+asyncpg://{config.postgres_user}:{config.postgres_password}@{config.postgres_host}:{config.postgres_port}/{config.postgres_db}")
    logger = create_logs()

    # init Bot
    bot: Bot = Bot(config.token.get_secret_value(), parse_mode="HTML")
    dp: Dispatcher = Dispatcher(bot=bot, storage=MemoryStorage(), repo=repo, logger=logger)

    # Register Handlers
    dp.include_router(base.router)  # Menu for users
    dp.include_router(main.router)  # Menu for admin
    dp.include_router(hash.router)  # Hashes
    dp.include_router(ciphers.router)  # Ciphers

    # filter registration
    dp.message.filter(F.chat.type == "private")

    # Register middlewares
    if config.limit != 0:
        dp.message.outer_middleware(AntiFloodMiddleware(config.limit))

    # Register /-commands in UI
    await set_commands(bot)

    logger.info("Start polling")

    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
