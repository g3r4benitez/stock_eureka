from fastapi import APIRouter, Depends, Security
from dependency_injector.wiring import inject, Provide
from starlette import status
from ratelimit.exception import RateLimitException


from app.services.alpha_service import AlphaService
from app.core.containers import ContainerService
from app.core.security.authentication import auth_required
from app.exceptions.general_exeptions import TooManyRequestException, BadRequestException
from app.core.config import SIMBOLS

router = APIRouter()

def validate_simbol(simbol: str):
    if simbol not in SIMBOLS:
        raise BadRequestException("simbol is not valid")
    return simbol


@router.get(
    "/{simbol}/{apikey}",
    name="get_stock_information",
    status_code=status.HTTP_200_OK,
)
@auth_required
@inject
def get_stock(
        alpha_service: AlphaService = Depends(Provide[ContainerService.alpha_service]),
        simbol: str = Depends(validate_simbol),
        apikey: str = None,
):
    try:
        return alpha_service.get_stock(simbol)
    except RateLimitException as error:
        raise TooManyRequestException


