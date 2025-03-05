from fastapi import Request
from fastapi.responses import RedirectResponse

from app.db.tables import service as service_table
from app.db.models import service as service_model

from app.settings import TEMPLATES


class ServiceController:

    def index(self, request: Request, name: str | None):
        services = service_table.select_many(name)
        return TEMPLATES.TemplateResponse("service.html", {
            "request": request,
            "services": services
        })

    def create_view(self, request: Request):
        return TEMPLATES.TemplateResponse("create_service.html", {
            "request": request
        })

    def create(self, service: service_model.InsertService):
        service_table.insert(
            (service.nome, service.categoria))
        return RedirectResponse(url="/", status_code=302)

    def edit(self, id: int, service: service_model.InsertService):
        service_table.update(
            id, (service.nome, service.categoria)
        )
        return RedirectResponse(url="/", status_code=303)

    def edit_view(self, request: Request, id: int):
        service = service_table.select_one(id, None)
        return TEMPLATES.TemplateResponse("edit_service.html", {
            "request": request,
            "service": service
        })

    def delete(self, id: int):
        service_table.delete(id)
        return RedirectResponse(url="/", status_code=302)
