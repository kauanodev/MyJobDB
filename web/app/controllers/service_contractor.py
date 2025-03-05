from fastapi import Request
from fastapi.responses import RedirectResponse

from app.db.tables import service_contractor as service_contractor_table
from app.db.models import service_contractor as service_contractor_model

from app.settings import TEMPLATES


class ServiceContractorController:

    def index(self, request: Request, name: str | None):
        users = service_contractor_table.select_many(name)
        return TEMPLATES.TemplateResponse("service_contractor.html", {
            "request": request,
            "users": users
        })

    def create_view(self, request: Request):
        return TEMPLATES.TemplateResponse("create_service_contractor.html", {
            "request": request,
        })

    def create(self, user: service_contractor_model.InsertServiceContractor):
        service_contractor_table.insert((user.usuario_id,))
        return RedirectResponse(url="/", status_code=302)

    def delete(self, id: int):
        service_contractor_table.delete(id)
        return RedirectResponse(url="/", status_code=302)
