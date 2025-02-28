from fastapi import Request, Response

from app.settings import TEMPLATES


class IndexController:

    def index(self, request: Request, response: Response):
        users = [
            {
                "id": 1,
                "nome": "cliclano",
                "cpf": "12345678902",
                "endereco": "Rua delclano",
                "data_de_nascimento": "12/12/00",
            },
            {
                "id": 2,
                "nome": "cliclano",
                "cpf": "12345678902",
                "endereco": "Rua delclano",
                "data_de_nascimento": "12/12/00",
            },
            {
                "id": 3,
                "nome": "cliclano",
                "cpf": "12345678902",
                "endereco": "Rua delclano",
                "data_de_nascimento": "12/12/00",
            },
        ]

        return TEMPLATES.TemplateResponse(
            "index.html", {"request": request, "users": users}
        )
