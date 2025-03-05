from typing import Annotated
from fastapi import APIRouter, Form, Path, Query, Request
from app.db.models import service_request as service_request_model
from app.controllers import service_request


router = APIRouter(tags=["service_request"])
controller = service_request.ServiceRequestController()


@router.get("/service-request")
def index(request: Request, name: Annotated[str | None, Query()] = None):
    return controller.index(request, name)


@router.get("/create-service-request")
def create_view(request: Request):
    return controller.create_view(request)


@router.post("/create-service-request")
def create(user_data: Annotated[
    service_request_model.InsertServiceRequest, Form()
]):
    return controller.create(user_data)


@router.get("/service-request/{id}")
def edit_view(request: Request, id: Annotated[int, Path()]):
    return controller.edit_view(request, id)


@router.post("/edit-service-request/{id}")
def edit(
    id: Annotated[int, Path()],
    user_data: Annotated[service_request_model.InsertServiceRequest, Form()]
):
    return controller.edit(id, user_data)


@router.post("/delete-service-request/{id}")
def delete(
    id: Annotated[int, Path()],
):
    return controller.delete(id)
