from fastapi import Request

from app.settings import TEMPLATES


class IndexController:

    def index(self, request: Request):
        return TEMPLATES.TemplateResponse("index.html", {
            "request": request,
        })
