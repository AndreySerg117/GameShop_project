from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from routers.main_page_router import router
from settings import settings
from pathlib import Path
import sentry_sdk

sentry_sdk.init(
    dsn=settings.SENTRY,
    send_default_pii=True,
)

BASE_DIR = Path(__file__).resolve().parent  # /app
STATIC_DIR = BASE_DIR / "static"

def get_application() -> FastAPI:
    app = FastAPI(debug=settings.DEBUG)
    app.include_router(router)

    app.mount('/static', StaticFiles(directory=STATIC_DIR), name='static')

    return app