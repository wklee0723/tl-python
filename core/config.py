import os
from dotenv import load_dotenv

load_dotenv()

#API_KEY = os.getenv("TWELVELABS_API_KEY")
#INDEX_ID = os.getenv("TWELVELABS_INDEX_ID")

# 시스템 환경 변수에서 직접 가져옵니다.
API_KEY = os.environ.get("TWELVELABS_API_KEY")
INDEX_ID = os.environ.get("TWELVELABS_INDEX_ID")

if not API_KEY:
    raise ValueError("TWELVELABS_API_KEY is not set")

if not INDEX_ID:
    raise ValueError("TWELVELABS_INDEX_ID is not set")