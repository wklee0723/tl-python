import pytest
from core.config import INDEX_ID
from utils.search_helper import safe_search


def test_search_invalid_index(client):
    result = safe_search(
        client,
        index_id="invalid_id",
        query_text="rocket",
        search_options=["visual"]
    )

    items = result["items"]
    error = result["error"]

    print("ITEMS::::::", items)
    print("ERROR::::::", error)

    # invalid index → API error 발생해야 정상
    assert error is not None
    assert "API_ERROR" in error


def test_search_empty_query(client):
    result = safe_search(
        client,
        index_id=INDEX_ID,
        query_text="",
        search_options=["visual"]
    )

    items = result["items"]
    error = result["error"]

    print("ITEMS::::::", items)
    print("ERROR::::::", error)

    # empty query → 보통 400 에러
    assert error is not None


def test_search_invalid_option(client):
    result = safe_search(
        client,
        index_id=INDEX_ID,
        query_text="rocket",
        search_options=["invalid"]
    )

    items = result["items"]
    error = result["error"]

    print("ITEMS::::::", items)
    print("ERROR::::::", error)

    # invalid option → 에러 발생해야 정상
    assert error is not None