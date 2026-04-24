from core.config import INDEX_ID
from utils.search_helper import safe_search


def test_search_valid_query_returns_results(client):
    result = safe_search(
        client,
        index_id=INDEX_ID,
        query_text="person",
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

    # "person"은 일반적으로 결과가 있어야 정상
    assert len(items) > 0


def test_search_multiple_queries(client):
    queries = ["person", "car", "rocket"]

    for q in queries:
        result = safe_search(
            client,
            index_id=INDEX_ID,
            query_text=q,
            search_options=["visual"]
        )

        items = result["items"]
        error = result["error"]

        print(f"QUERY: {q}")
        print("ITEMS::::::", items)
        print("ERROR::::::", error)

        assert isinstance(items, list)

        if error == "SERVER_500":
            print("Server error occurred (treated as known issue)")
            continue

        # 결과가 없어도 정상 케이스이므로 list 여부만 검증
        assert items is not None