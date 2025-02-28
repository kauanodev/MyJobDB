from typing import Annotated
from fastapi import APIRouter, Form
from app.controllers import user


router = APIRouter(tags=["user"])
controller = user.UserController()


@router.post("/create-user")
def index(email: Annotated[str, Form()], password: Annotated[str, Form()]):
    user_data = user.UserDataForm(email=email, password=password)
    return controller.create(user_data)
