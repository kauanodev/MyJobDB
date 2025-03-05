from typing import Annotated
from fastapi import APIRouter, Form, Path, Query, Request
from app.db.models import service_contractor as service_contractor_model
from app.controllers import service_contractor


router = APIRouter(tags=["service_contractor"])
controller = service_contractor.ServiceContractorController()


@router.get("/service-contractor")
def index(request: Request, name: Annotated[str | None, Query()] = None):
    return controller.index(request, name)


@router.get("/create-service-contractor")
def create_view(request: Request):
    return controller.create_view(request)


@router.post("/create-service-contractor")
def create(user_data: Annotated[
    service_contractor_model.InsertServiceContractor, Form()
]):
    return controller.create(user_data)


@router.post("/delete-service-contractor/{id}")
def delete(
    id: Annotated[int, Path()],
):
    return controller.delete(id)
