from uvicorn import run as run_asgi

from backend import app
from backend.db import AsyncDB
from backend.utils import hash_pwd


if __name__ == "__main__":
    AsyncDB.migrate()
    AsyncDB.create_mock_data(hash_func=hash_pwd)
    run_asgi(app=app, port=8134)
