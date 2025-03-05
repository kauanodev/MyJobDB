from typing import Annotated
from fastapi import APIRouter, Form, Path, Query, Request
from app.db.models import service as service_model
from app.controllers import service


router = APIRouter(tags=["service"])
controller = service.ServiceController()


@router.get("/service")
def index(request: Request, name: Annotated[str | None, Query()] = None):
    return controller.index(request, name)


@router.get("/create-service")
def create_view(request: Request):
    return controller.create_view(request)


@router.post("/create-service")
def create(service_data: Annotated[service_model.InsertService, Form()]):
    return controller.create(service_data)


@router.get("/service/{id}")
def edit_view(request: Request, id: Annotated[int, Path()]):
    return controller.edit_view(request, id)


@router.post("/edit-service/{id}")
def edit(
    id: Annotated[int, Path()],
    service_data: Annotated[service_model.InsertService, Form()]
):
    return controller.edit(id, service_data)


@router.post("/delete-service/{id}")
def delete(
    id: Annotated[int, Path()],
):
    return controller.delete(id)
