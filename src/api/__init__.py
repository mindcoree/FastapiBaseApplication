from fastapi import APIRouter
from .users.views import router as router_users
from core.config import settings

router = APIRouter()

router.include_router(router_users, prefix=settings.api.users.prefix)


# Динамически импортируем все роутеры из папок
# for path in Path(__file__).parent.glob("*/views.py"):
#     module_name = f"api.{path.parent.name}.views"
#     module = import_module(module_name)
#     if hasattr(module, "router"):
#         router.include_router(module.router, prefix=f"/{path.parent.name}")
