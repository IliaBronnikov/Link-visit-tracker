def test_create_item_good_data(redis_test_db, client):
    data = {
        "links": [
            "https://ya.ru",
            "https://ya.ru?q=123",
            "funbox.ru",
            "https://stackoverflow.com/questions/11828270/how-to-exit-the-vim-editor",
        ]
    }

    response = client.post(
        "/visited_links/", headers={"Content-Type": "application/json"}, json=data
    )

    assert response.status_code == 200
    assert len(redis_test_db.redis_db.xrange(redis_test_db.stream)) == 4
    assert response.json()["status"] == "ok"


def test_create_item_wrong_data(redis_test_db, client):
    data = {"links": []}

    response = client.post(
        "/visited_links/", headers={"Content-Type": "application/json"}, json=data
    )

    assert response.status_code == 200
    assert response.json()["status"] == "No links"


def test_read_item_good_data(redis_test_db, client):
    data = {
        "links": [
            "https://ya.ru",
            "https://ya.ru?q=123",
            "funbox.ru",
            "https://stackoverflow.com/questions/11828270/how-to-exit-the-vim-editor",
        ]
    }

    client.post(
        "/visited_links/", headers={"Content-Type": "application/json"}, json=data
    )
    response = client.get("/visited_domains?start=13&end=9999999999999")

    assert response.status_code == 200
    assert response.json()["status"] == "ok"
    assert len(response.json()["domains"]) == 3


def test_read_item_wrong_data(redis_test_db, client):
    data = {
        "links": [
            "https://ya.ru",
            "https://ya.ru?q=123",
            "funbox.ru",
            "https://stackoverflow.com/questions/11828270/how-to-exit-the-vim-editor",
        ]
    }

    client.post(
        "/visited_links/", headers={"Content-Type": "application/json"}, json=data
    )
    response = client.get("/visited_domains?start=tr&end=9999999999999")

    assert response.status_code == 200
    assert (
        response.json()["status"]
        == "Wrong time format. Example: api/visited_domains/?start=0&end=16"
    )
