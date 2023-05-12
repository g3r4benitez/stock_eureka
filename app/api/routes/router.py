from fastapi import APIRouter

from app.controllers import ping_controller as ping
from app.controllers import stock_controller as router_stock
from app.controllers import user_controller as router_user

from app.core.config import API_PREFIX

api_router = APIRouter(prefix=API_PREFIX)
api_router.include_router(router_stock.router, tags=["stock"], prefix="/stock")
api_router.include_router(router_user.router, tags=["user"], prefix="/user")
api_router.include_router(ping.router, tags=["ping"], prefix="/ping")
