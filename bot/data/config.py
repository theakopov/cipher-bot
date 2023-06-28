import logging
from pydantic import BaseSettings, SecretStr


class Settings(BaseSettings):
    # Bot settings
    token: SecretStr
    admin: int
    limit: int
    key: SecretStr

    # Databases

    # Postgresql
    postgres_user: str
    postgres_password: str
    postgres_db: str
    postgres_host: str
    postgres_port: int

    # Redis

    redis_host: str
    redis_port: int
    redis_db: int

    class Config:
        pass
        env_file = ".env"
        env_file_encoding = "utf-8"


config = Settings()


# logging
formatter = logging.Formatter("[%(asctime)s] - %(message)s")

logger = logging.getLogger('usage')
logger.setLevel(logging.INFO)

console_handler = logging.StreamHandler()

file_handler = logging.FileHandler('logs.log')

console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)
