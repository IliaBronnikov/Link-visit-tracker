import os

REDIS_HOST = os.getenv("REDIS_HOST", default="localhost")
REDIS_PORT = os.getenv("REDIS_PORT", default=6379)
REDIS_STREAM = 'url_history'
