from fastapi import FastAPI

from routers.main_page_router import router
from settings import settings

import sentry_sdk

sentry_sdk.init(
    dsn=settings.SENTRY,
    send_default_pii=True,
)

def get_application() -> FastAPI:
    app = FastAPI(debug=settings.DEBUG)
    app.include_router(router)

    return app