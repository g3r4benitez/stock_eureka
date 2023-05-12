from functools import wraps

from app.repositories import user_repository
from app.exceptions.general_exeptions import UnauthorizedException


def auth_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        apikey = kwargs.get('apikey')
        if not user_repository.get_user_using_apikey(apikey):
            raise UnauthorizedException("Apikey is not valid")
        return func(*args, **kwargs)
    return wrapper
