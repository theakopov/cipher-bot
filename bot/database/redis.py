import redis

from ..data.config import config


class Cache:
    """
    Class for working with cache through redis
    """

    def __init__(self, time_limit: int | float = 0.7):
        self.redis = redis.Redis(
            host=config.redis_host, port=config.redis_port, db=config.redis_db)
        self.LIMIT = time_limit

    def add_user(self, user_id: int):
        self.redis.set(name=str(user_id), value="", px=self.LIMIT)

    def check_user(self, user_id: int):
        return str(user_id).encode() in self.redis.keys()
