import uvicorn
import logging
from fastapi import FastAPI, status
from fastapi.requests import Request
from fastapi.middleware.cors import CORSMiddleware
from app.core.initializer import init

from app.api.routes.router import api_router
from app.core.config import (APP_NAME, APP_VERSION,
                             IS_DEBUG)
from app.core.error_handler import HTTPCustomException, exception_handler, fatal_exception_handler

# setup loggers
from os import path
log_file_path = path.join(path.dirname(path.abspath(__file__)), 'loggin.conf')
logging.config.fileConfig(log_file_path)

# get root logger
logger = logging.getLogger(__name__)


def start_app() -> FastAPI:
    fast_app = FastAPI(title=APP_NAME, version=APP_VERSION, debug=IS_DEBUG)
    # Routes
    fast_app.include_router(api_router)

    # Middleware
    fast_app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    # Error handlers
    fast_app.add_exception_handler(HTTPCustomException, exception_handler)
    fast_app.add_exception_handler(status.HTTP_500_INTERNAL_SERVER_ERROR, fatal_exception_handler)
    return fast_app


app = start_app()
init(app)


@app.middleware("http")
async def log_requests(request: Request, call_next):
    logger.info(f"start request path={request.url.path}")
    q = request.query_params
    p = request.path_params
    h = request.headers
    logger.info(f"Query Parameters: {q}")
    logger.info(f"Path Parameters: {p}")
    logger.info(f"Headers: {h}")

    response = await call_next(request)

    logger.info(f"Response status_code={response.status_code}")

    return response

if __name__ == '__main__':
    uvicorn.run('app.main:app', host='0.0.0.0', port=8000, reload=True)
