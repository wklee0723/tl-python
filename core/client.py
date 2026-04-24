import os
from dotenv import load_dotenv
from twelvelabs import TwelveLabs

load_dotenv()

def get_client():
    api_key = os.getenv("TWELVELABS_API_KEY")

    if not api_key:
        raise ValueError("API key not found")

    client = TwelveLabs(api_key=api_key)
    return client