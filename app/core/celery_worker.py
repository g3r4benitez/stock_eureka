from celery.utils.log import get_task_logger


from app.services.setup_service import SetupService
from .celery_app import celery_app

celery_log = get_task_logger(__name__)

setup_service = SetupService()


@celery_app.task(
    name='app.core.celery_worker.dummy_task',
    queue="queue_name",
    )
def update_tab_task():
    pass


