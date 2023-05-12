from fastapi import APIRouter
from starlette import status

from app.models.user import User
from app.repositories import user_repository


router = APIRouter()


@router.post(
    "",
    name="user_create",
    status_code=status.HTTP_201_CREATED,
    dependencies=[]
)
async def post_create(user: User):
    user = user_repository.create(user)
    return user.apikey

@router.get(
    "",
    name="user_get",
    status_code=status.HTTP_200_OK,
    dependencies=[]
)
async def get_user(email: str):
    return user_repository.get(email)
