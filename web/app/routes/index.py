from fastapi import APIRouter, Request
from app.controllers import index


router = APIRouter(tags=["index"])
controller = index.IndexController()


@router.get("/")
def index(request: Request):
    return controller.index(request)
