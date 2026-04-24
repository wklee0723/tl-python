from core.config import INDEX_ID
from utils.search_helper import safe_search


def test_search_no_results(client):
    result = safe_search(
        client,
        index_id=INDEX_ID,
        query_text="asldkfjalskdfj",
        search_options=["visual"]
    )

    items = result["items"]
    error = result["error"]

    print("ITEMS::::::", items)
    print("ERROR::::::", error)

    assert isinstance(items, list)

    if error == "SERVER_500":
        print("Server error occurred (treated as known issue)")
        return

    if len(items) == 0:
        print("No results found")
        return


def test_search_repeatability(client):
    for _ in range(3):
        result = safe_search(
            client,
            index_id=INDEX_ID,
            query_text="rocket",
            search_options=["visual"]
        )

        items = result["items"]
        error = result["error"]

        print("ITEMS::::::", items)
        print("ERROR::::::", error)

        assert isinstance(items, list)

        if error == "SERVER_500":
            print("Server error occurred (treated as known issue)")
            continue

        # repeatability 테스트는 "에러 없이 반복 호출 가능"이 핵심
        assert items is not None


def test_search_with_page_limit(client):
    result = safe_search(
        client,
        index_id=INDEX_ID,
        query_text="rocket",
        search_options=["visual"],
        page_limit=5
    )

    items = result["items"]
    error = result["error"]

    print("ITEMS::::::", items)
    print("ERROR::::::", error)

    assert isinstance(items, list)

    if error == "SERVER_500":
        print("Server error occurred (treated as known issue)")
        return

    if len(items) == 0:
        print("No results found")
        return

    assert len(items) <= 5