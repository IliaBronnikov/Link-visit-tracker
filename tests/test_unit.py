from datetime import datetime
from services import set_links, get_links_in_range


def test_write_data_redis(redis_test_db):
    data = {
        "links": [
            "https://ya.ru",
            "https://ya.ru?q=123",
            "funbox.ru",
            "https://stackoverflow.com/questions/11828270/how-to-exit-the-vim-editor",
        ]
    }

    set_links(data, redis_test_db)

    assert redis_test_db.redis_db.xlen(redis_test_db.stream) == 4


def test_read_data_redis(redis_test_db):
    time_now = int(datetime.timestamp(datetime.now()) * 1000)
    data = {
        "links": [
            "https://ya.ru",
            "https://ya.ru?q=123",
            "funbox.ru",
            "https://stackoverflow.com/questions/11828270/how-to-exit-the-vim-editor",
        ]
    }

    set_links(data, redis_test_db)
    data = get_links_in_range(time_now - 100, time_now + 100000000000, redis_test_db)

    assert len(data["domains"]) == 3
