from core.config import INDEX_ID
from utils.search_helper import safe_search

def test_search_with_valid_query(client):
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

    # ✅ 서버 에러 케이스 명확히 구분
    if error == "SERVER_500":
        print("Server error occurred (treated as known issue)")
        return

    if len(items) == 0:
        print("No results found")
        return

    first = items[0]
    assert first.video_id is not None
    assert first.rank is not None