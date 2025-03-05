from fastapi import APIRouter, Request, Response
from app.controllers import index


router = APIRouter(tags=["index"])
controller = index.IndexController()


@router.get("/")
def index(request: Request, response: Response):
    return controller.index(request, response)
