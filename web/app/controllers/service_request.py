from fastapi import Request
from fastapi.responses import RedirectResponse

from app.db.tables import service_request as service_request_table
from app.db.models import service_request as service_request_model

from app.settings import TEMPLATES


class ServiceRequestController:

    def index(self, request: Request, name: str | None):
        service_requests = service_request_table.select_many(name)
        return TEMPLATES.TemplateResponse("service_request.html", {
            "request": request,
            "service_requests": service_requests
        })

    def create_view(self, request: Request):
        return TEMPLATES.TemplateResponse("create_service_request.html", {
            "request": request,
        })

    def create(self, service_request: service_request_model.InsertServiceRequest):
        service_request_table.insert((
            service_request.preco,
            service_request.prazo,
            None if service_request.descricao == "" else service_request.descricao,
            service_request.servico_id,
            service_request.contratante_id,
            None if service_request.prestador_id == 0 else service_request.prestador_id
        ))
        return RedirectResponse(url="/", status_code=302)

    def edit(self, id: int, service_request: service_request_model.InsertServiceRequest):
        service_request_table.update(id, (
            service_request.preco,
            service_request.prazo,
            None if service_request.descricao == "" else service_request.descricao,
            service_request.servico_id,
            service_request.contratante_id,
            None if service_request.prestador_id == 0 else service_request.prestador_id
        ))
        return RedirectResponse(url="/", status_code=303)

    def edit_view(self, request: Request, id: int):
        service_request = service_request_table.select_one(id, None)
        return TEMPLATES.TemplateResponse("edit_service_request.html", {
            "request": request,
            "service_request": service_request_model.SelectServiceRequest(
                id=service_request["id"],
                preco=service_request["preco"],
                prazo=service_request["prazo"].isoformat().replace(
                    "T00:00:00", ""),
                descricao="" if service_request["descricao"] is None else service_request["descricao"],
                servico_id=service_request["servico_id"],
                contratante_id=service_request["contratante_id"],
                prestador_id=0 if service_request["prestador_id"] is None else service_request["prestador_id"]
            ),
        })

    def delete(self, id: int):
        service_request_table.delete(id)
        return RedirectResponse(url="/", status_code=302)
