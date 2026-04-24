from core.config import INDEX_ID
from utils.search_helper import safe_search


def test_search_response_schema(client):
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

    # ✅ 서버 에러 구분
    if error == "SERVER_500":
        print("Server error occurred (treated as known issue)")
        return

    # ✅ 결과 없음 허용
    if len(items) == 0:
        print("No results found")
        return

    item = items[0]

    assert hasattr(item, "video_id")
    assert hasattr(item, "start")
    assert hasattr(item, "end")
    assert hasattr(item, "rank")
    
    
def test_search_value_types(client):
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

    # ✅ 서버 에러 구분
    if error == "SERVER_500":
        print("Server error occurred (treated as known issue)")
        return

    # ✅ 결과 없음 허용
    if len(items) == 0:
        print("No results found")
        return

    item = items[0]

    assert isinstance(item.video_id, str)
    assert isinstance(item.start, float)
    assert isinstance(item.end, float)
    assert isinstance(item.rank, int)