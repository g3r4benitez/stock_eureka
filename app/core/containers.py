from dependency_injector import containers, providers
from app.services.alpha_service import AlphaService


class ContainerService(containers.DeclarativeContainer):
    alpha_service = providers.Singleton(
        AlphaService
    )