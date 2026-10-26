"""Part 2: tests against JSONPlaceholder, a public API.

Complete API_FINDINGS.md before writing any test in this file. Each
assertion below should state what you recorded there, not a value
copied from the documentation.

Run with:
    pytest test_public_api.py -v
"""
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def test_get_single_post():
    """GET /posts/1."""
    response = requests.get(f"{BASE_URL}/posts/1")

    assert response.status_code == 200
    assert response.headers.get("Content-Type") == "application/json; charset=utf-8"

    body = response.json()

    assert isinstance(body, dict)
    assert "userId" in body
    assert isinstance(body["userId"], int)
    assert "id" in body
    assert isinstance(body["id"], int)
    assert "title" in body
    assert isinstance(body["title"], str)
    assert "body" in body
    assert isinstance(body["body"], str)


def test_get_all_posts():
    """GET /posts."""
    response = requests.get(f"{BASE_URL}/posts")

    assert response.status_code == 200
    assert response.headers.get("Content-Type") == "application/json; charset=utf-8"

    body = response.json()

    assert isinstance(body, list)
    assert len(body) == 100

    for post in body:
        assert isinstance(post, dict)
        assert isinstance(post["userId"], int)
        assert isinstance(post["id"], int)
        assert isinstance(post["title"], str)
        assert isinstance(post["body"], str)


def test_create_post():
    """POST /posts."""
    payload = {
        "title": "API testing",
        "body": "Testing POST requests",
        "userId": 1
    }

    response = requests.post(
        f"{BASE_URL}/posts",
        json=payload
    )

    assert response.status_code == 201
    assert response.headers.get("Content-Type") == "application/json; charset=utf-8"

    body = response.json()

    assert body["title"] == payload["title"]
    assert body["body"] == payload["body"]
    assert body["userId"] == payload["userId"]
    assert "id" in body
    assert isinstance(body["id"], int)
    assert body["id"] == 101


def test_delete_post():
    """DELETE /posts/1."""
    response = requests.delete(f"{BASE_URL}/posts/1")

    assert response.status_code == 200
    assert response.headers.get("Content-Type") == "application/json; charset=utf-8"

