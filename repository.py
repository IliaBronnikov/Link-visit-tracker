from abc import ABC
import config
import redis


class StreamRepository(ABC):
    def __init__(self):
        ...

    def get(self, start: int, end: int) -> set:
        ...

    def set(self, value: str) -> None:
        ...


class RedisRepository(StreamRepository):
    def __init__(self):
        super().__init__()
        self.redis_db = redis.StrictRedis(
            host=config.REDIS_HOST, port=config.REDIS_PORT, db=0
        )
        self.stream = config.REDIS_STREAM

    def get(self, start: int, end: int) -> set:
        links_range = self.redis_db.xrange(self.stream, start, end)
        unique_links = {link[b"link"].decode("utf-8") for _, link in links_range}
        return unique_links

    def set(self, value: str):
        self.redis_db.xadd(self.stream, {"link": value})
