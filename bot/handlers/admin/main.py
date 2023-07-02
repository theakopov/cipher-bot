from aiogram.filters import Command
from aiogram.types import Message, input_file
from aiogram import Router
from textwrap import dedent

from ...database.requests import Repository
from ...data.config import config as config_
from ...filters import ForAdmins

router = Router()


@router.message(Command("stat"), ForAdmins())
async def get_statistic(message: Message, repo: Repository, *args, **kwargs):
    """
    Returns the number of bot users
    """
    result = await repo.get_stat()
    await message.answer(f"Users: {result}")


@router.message(Command("config"), ForAdmins())
async def config(message: Message, *args, **kwargs):
    """"
    Returns bot settings
    """
    await message.answer(
        dedent(f"""
    <b>Bot config:</b>

    Token: <code>{config_.token.get_secret_value()}</code>
    Admin: <code>{config_.admin}</code>
    Time limit: <code>{config_.limit} milliseconds</code>

    <b>Postgres:</b>
    User: <code>{config_.postgres_user}</code>
    Password: <code>{config_.postgres_password}</code>
    Host: <code>{config_.postgres_host}</code>
    DB Name: <code>{config_.postgres_db}</code>
    Port: <code>{config_.postgres_port}</code>

    <b>Redis:</b>
    Host: <code>{config_.redis_host}</code>
    Port: <code>{config_.redis_port}</code>
    DB: <code>{config_.redis_db}</code>
        """))


@router.message(Command("logs"), ForAdmins())
async def logs(message: Message, *args, **kwargs):
    logs = input_file.FSInputFile("logs.log")
    await message.answer_document(logs)
