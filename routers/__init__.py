from fastapi import APIRouter

from . import public


router = APIRouter(prefix = '/cars')

router.include_router(public.router)
