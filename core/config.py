import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("TWELVELABS_API_KEY")
INDEX_ID = os.getenv("TWELVELABS_INDEX_ID")

if not API_KEY:
    raise ValueError("TWELVELABS_API_KEY is not set")

if not INDEX_ID:
    raise ValueError("TWELVELABS_INDEX_ID is not set")