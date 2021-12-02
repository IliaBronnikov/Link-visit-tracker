import pytest
from fastapi.testclient import TestClient

from main import app
from repository import RedisRepository


@pytest.fixture()
def redis_test_db():
    redis_test_repository = RedisRepository()
    yield redis_test_repository
    redis_test_repository.redis_db.delete(redis_test_repository.stream)


@pytest.fixture()
def client():
    return TestClient(app)
