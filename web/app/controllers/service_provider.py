from fastapi import Request
from fastapi.responses import RedirectResponse

from app.db.tables import service_provider as service_provider_table
from app.db.models import service_provider as service_provider_model

from app.settings import TEMPLATES


class ServiceProviderController:

    def index(self, request: Request, name: str | None):
        users = service_provider_table.select_many(name)
        return TEMPLATES.TemplateResponse("service_provider.html", {
            "request": request,
            "users": users
        })

    def create_view(self, request: Request):
        return TEMPLATES.TemplateResponse("create_service_provider.html", {
            "request": request,
        })

    def create(self, user: service_provider_model.InsertServiceProvider):
        service_provider_table.insert(
            (user.usuario_id, user.informacoes_adicionais))
        return RedirectResponse(url="/", status_code=302)

    def edit(self,
             id: int,
             user: service_provider_model.InsertServiceProvider):
        service_provider_table.update(
            id, (user.usuario_id, user.informacoes_adicionais))
        return RedirectResponse(url="/", status_code=303)

    def edit_view(self, request: Request, id: int):
        user = service_provider_table.select_one(id, None)
        return TEMPLATES.TemplateResponse("edit_service_provider.html", {
            "request": request,
            "user": user
        })

    def delete(self, id: int):
        service_provider_table.delete(id)
        return RedirectResponse(url="/", status_code=302)
