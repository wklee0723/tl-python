from twelvelabs.core.api_error import ApiError

def safe_search(client, **kwargs):
    try:
        items = list(client.search.query(**kwargs))
        return {
            "items": items,
            "error": None
        }
    except ApiError as e:
        if e.status_code == 500:
            return {
                "items": [],
                "error": "SERVER_500"
            }
        return {
            "items": [],
            "error": f"API_ERROR_{e.status_code}"
        }