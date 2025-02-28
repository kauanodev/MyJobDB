from fastapi import Request, Response
from fastapi.responses import RedirectResponse
from pydantic import BaseModel


class UserDataForm(BaseModel):
    email: str
    password: str


class UserController:

    def create(self, user: UserDataForm):
        print(user)
        return RedirectResponse(url="/", status_code=302)
