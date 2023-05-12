from fastapi import APIRouter, Depends
from dependency_injector.wiring import inject, Provide
from starlette import status
from ratelimit.exception import RateLimitException

from fastapi.security.api_key import APIKey

from app.services.alpha_service import AlphaService
from app.core.containers import ContainerService
from app.exceptions.general_exeptions import TooManyRequestException, BadRequestException
from app.core.config import SIMBOLS
from app.core.security.authentication import validate_api_key


router = APIRouter()


def validate_simbol(simbol: str):
    if simbol not in SIMBOLS:
        raise BadRequestException("simbol is not valid")
    return simbol


@router.get(
    "/{simbol}",
    name="get_stock_information",
    status_code=status.HTTP_200_OK,
)
@inject
def get_stock(
        alpha_service: AlphaService = Depends(Provide[ContainerService.alpha_service]),
        simbol: str = Depends(validate_simbol),
        api_key: APIKey = Depends(validate_api_key),
):
    try:
        return alpha_service.get_stock(simbol)
    except RateLimitException as error:
        raise TooManyRequestException


