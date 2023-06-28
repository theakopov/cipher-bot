from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeAllPrivateChats


async def set_commands(bot: Bot):
    """Register /-commands in UI"""
    commands = [
        BotCommand(command="start", description="launch bot"),
        BotCommand(command="help", description="usage guide"),
    ]
    await bot.set_my_commands(commands=commands, scope=BotCommandScopeAllPrivateChats())
