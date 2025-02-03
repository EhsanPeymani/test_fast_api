import threading
import time
import uvicorn
from fastapi import FastAPI
from my_utility import get_service
from my_route import router
from my_service import MyService


def update_service_continuously():
    service = get_service()
    while True:
        service.update()
        time.sleep(1)


if __name__ == "__main__":
    app = FastAPI()
    app.include_router(router)
    app.dependency_overrides[MyService] = lambda: get_service()

    thread = threading.Thread(target=update_service_continuously, daemon=True)
    thread.start()

    uvicorn.run(app, host="0.0.0.0", port=8000)
