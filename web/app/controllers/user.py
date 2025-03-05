from fastapi import Request
from fastapi.responses import RedirectResponse

from app.db.tables import user as user_table
from app.db.models import user as user_model

from app.settings import TEMPLATES


class UserController:

    def index(self, request: Request, name: str | None):
        users = user_table.select_many(name)
        return TEMPLATES.TemplateResponse("user.html", {
            "request": request,
            "users": users
        })

    def create_view(self, request: Request):
        return TEMPLATES.TemplateResponse("create_user.html", {
            "request": request,
        })

    def create(self, user: user_model.InsertUser):
        user_table.insert(
            (user.nome, user.cpf, user.endereco, user.data_de_nascimento))
        return RedirectResponse(url="/", status_code=302)

    def edit(self, id: int, user: user_model.InsertUser):
        user_table.update(
            id,
            (user.nome, user.cpf, user.endereco, user.data_de_nascimento)
        )
        return RedirectResponse(url="/", status_code=303)

    def edit_view(self, request: Request, id: int):
        user = user_table.select_one(id, None)
        return TEMPLATES.TemplateResponse("edit_user.html", {
            "request": request,
            "user": user_model.SelectUser(
                id=user["id"],
                nome=user["nome"],
                cpf=user["cpf"],
                endereco=user["endereco"],
                data_de_nascimento=user["data_de_nascimento"].isoformat(),
            )
        })

    def delete(self, id: int):
        user_table.delete(id)
        return RedirectResponse(url="/", status_code=302)
