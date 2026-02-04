import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_URL = os.getenv("INGESTION_API_URL")
TOKEN = os.getenv("CONNECTOR_TOKEN")


def upload_file(path: str):
    with open(path, "rb") as f:
        response = requests.post(
            API_URL,
            headers={"Authorization": f"Bearer {TOKEN}"},
            files={"file": f}
        )

    print(response.status_code)
    print(response.json())


if __name__ == "__main__":
    upload_file("sample_tally.xml")
