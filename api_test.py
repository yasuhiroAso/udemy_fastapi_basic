import requests
import json
from datetime import datetime


def main():
    url = "http://localhost:8000/contacts"
    current_datetime = datetime.now().isoformat()
    body = {
        "id": 1,
        "name": "山田太郎さん",
        "email": "test1@test.com",
        "url": "https://example.com",
        "gender": 2,
        "message": "メッセージです",
        "is_enabled": True,
        "created_at": current_datetime,
    }
    print("実行中")
    print(json.dumps(body))

    res = requests.post(url, json.dumps(body))
    print(res)
    print(res.json())


if __name__ == "__main__":
    main()
