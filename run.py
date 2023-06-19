import json
import os
from typing import Dict
import requests
from dotenv import load_dotenv

load_dotenv()


@staticmethod
def _request():
    CHATGPT_API_URL: str = os.getenv("CHATGPT_API_URL", "")
    return requests.post(CHATGPT_API_URL, headers=_mount_headers(), data=_mount_body())


@staticmethod
def _mount_headers() -> Dict:
    CHATGPT_API_KEY: str = os.getenv("CHATGPT_API_KEY", "")
    return {
        "Authorization": f"Bearer {CHATGPT_API_KEY}",
        "Content-Type": "application/json",
    }


@staticmethod
def _mount_body():
    script = "Olá chat!"

    return json.dumps(
        {
            "model": "gpt-3.5-turbo",
            "messages": [
                {"role": "user", "content": script},
            ],
        }
    )


result = _request()

if result.status_code == 200:
    data = result.json()
    print(data)
else:
    print(result.json())
