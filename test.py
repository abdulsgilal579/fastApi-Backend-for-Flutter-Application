import requests

response = requests.post(
    "http://127.0.0.1:8000/ask",
    json={
        "question": "Who was JFK?"
    }
)

print(response.json())