import logging
from django.conf import settings
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django.core.management.base import BaseCommand
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution
from django_apscheduler import util
from django.core.management import BaseCommand


from mailing.task import send_mailing_plural

from mailing.utils import get_mailing_period_trigger
from mailing.models import Mailing


logger = logging.getLogger(__name__)


class Command(BaseCommand):

    def handle(self, *args, **options):
        send_mailing_plural()

    # help = "Runs APScheduler."
    #
    # def handle(self, *args, **options):
    #     from mailing.receivers import delete_job, schedule_job, scheduler  # noqa: F401
    #
    #     if not scheduler.running:
    #         scheduler.start()
    #         logger.info('Scheduler started')

    # def handle(self, *args, **options):
    #     scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
    #     scheduler.add_jobstore(DjangoJobStore(), "default")
    #     mailing = Mailing()
    #     trigger = get_mailing_period_trigger(mailing)
    #
    #     scheduler.add_job(
    #         send_mailing,
    #         trigger=trigger,  # Every 10 seconds
    #         id="send_mailing",  # The `id` assigned to each job MUST be unique
    #         max_instances=1,
    #         replace_existing=True,
    #     )
    #
    #     try:
    #         logger.info("Starting scheduler...")
    #         scheduler.start()
    #     except KeyboardInterrupt:
    #         logger.info("Stopping scheduler...")
    #         scheduler.shutdown()
    #         logger.info("Scheduler shut down successfully!")