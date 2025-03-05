from typing import Annotated
from fastapi import APIRouter, Form, Path, Query, Request
from app.db.models import service_provider as service_provider_model
from app.controllers import service_provider


router = APIRouter(tags=["service_provider"])
controller = service_provider.ServiceProviderController()


@router.get("/service-provider")
def index(request: Request, name: Annotated[str | None, Query()] = None):
    return controller.index(request, name)


@router.get("/create-service-provider")
def create_view(request: Request):
    return controller.create_view(request)


@router.post("/create-service-provider")
def create(user_data: Annotated[
    service_provider_model.InsertServiceProvider, Form()
]):
    return controller.create(user_data)


@router.get("/service-provider/{id}")
def edit_view(request: Request, id: Annotated[int, Path()]):
    return controller.edit_view(request, id)


@router.post("/edit-service-provider/{id}")
def edit(
    id: Annotated[int, Path()],
    user_data: Annotated[service_provider_model.InsertServiceProvider, Form()]
):
    return controller.edit(id, user_data)


@router.post("/delete-service-provider/{id}")
def delete(
    id: Annotated[int, Path()],
):
    return controller.delete(id)
