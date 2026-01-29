import os
from app.core.config import RAW_STORAGE_PATH

def save_raw_file(upload_id: str, file):
    os.makedirs(RAW_STORAGE_PATH, exist_ok=True)

    file_path = os.path.join(
        RAW_STORAGE_PATH,
        f"{upload_id}_{file.filename}"
    )

    with open(file_path, "wb") as f:
        f.write(file.file.read())

    if not os.path.exists(file_path):
        raise RuntimeError("File write failed")

    return file_path