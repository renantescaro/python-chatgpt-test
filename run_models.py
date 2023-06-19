import json
import os
from typing import Dict
import requests
from dotenv import load_dotenv

load_dotenv()


@staticmethod
def _request_models():
    CHATGPT_API_URL: str = os.getenv("CHATGPT_API_URL", "")
    return requests.get(CHATGPT_API_URL, headers=_mount_headers())


@staticmethod
def _mount_headers() -> Dict:
    CHATGPT_API_MODELS_URL: str = os.getenv("CHATGPT_API_MODELS_URL", "")
    return {"Authorization": f"Bearer {CHATGPT_API_MODELS_URL}"}


result = _request_models()

if result.status_code == 200:
    data = result.json()
    id = "gpt-3.5-turbo"
else:
    print(result)
