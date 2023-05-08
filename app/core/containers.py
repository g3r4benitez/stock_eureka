from dependency_injector import containers, providers
from app.services.dummy_service import DummyService


class ContainerService(containers.DeclarativeContainer):
    dummy_service = providers.Singleton(
        DummyService
    )