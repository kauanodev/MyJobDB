from typing import Annotated
from fastapi import APIRouter, Form, Path, Query, Request
from app.db.models import user as user_model
from app.controllers import user


router = APIRouter(tags=["user"])
controller = user.UserController()


@router.get("/user")
def index(request: Request, name: Annotated[str | None, Query()] = None):
    return controller.index(request, name)


@router.get("/create-user")
def create_view(request: Request):
    return controller.create_view(request)


@router.post("/create-user")
def create(user_data: Annotated[user_model.InsertUser, Form()]):
    return controller.create(user_data)


@router.get("/user/{id}")
def edit_view(request: Request, id: Annotated[int, Path()]):
    return controller.edit_view(request, id)


@router.post("/edit-user/{id}")
def edit(
    id: Annotated[int, Path()],
    user_data: Annotated[user_model.InsertUser, Form()]
):
    return controller.edit(id, user_data)


@router.post("/delete-user/{id}")
def delete(
    id: Annotated[int, Path()],
):
    return controller.delete(id)
