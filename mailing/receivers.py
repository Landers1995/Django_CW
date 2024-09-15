import logging
from logging import shutdown

from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

#from mailing.jobs import schedule_mailing
from mailing.task import send_mailing
from mailing.models import Mailing
#from mailing.scheduler import scheduler
from mailing.utils import get_mailing_period_trigger
from apscheduler.schedulers.background import BackgroundScheduler, BlockingScheduler
from django_apscheduler.jobstores import DjangoJobStore
from django.conf import settings

logger = logging.getLogger(__name__)

scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
scheduler.add_jobstore(DjangoJobStore(), 'default')


@receiver(post_save, sender=Mailing)
def schedule_job(instance: Mailing, created: bool, **kwargs):
    job_id = f'schedule_{instance.pk}'
    trigger = get_mailing_period_trigger(instance)
    if created:
        scheduler.add_job(
            send_mailing,
            id=job_id,
            trigger=trigger,
            args=[instance.pk],
            max_instances=1,
            replace_existing=True,
        )
        logger.info('Job %s created', job_id)
        scheduler.wakeup()
    else:
        scheduler.reschedule_job(job_id=job_id, trigger=trigger)
        logger.info('Job %s updated', job_id)

    if instance.is_active:
        scheduler.resume_job(job_id=job_id)
    else:
        scheduler.pause_job(job_id=job_id)


@receiver(post_delete, sender=Mailing)
def delete_job(instance: Mailing, **kwargs):
    job_id = f'schedule_{instance.pk}'
    job = scheduler.get_job(job_id)
    if job:
        scheduler.remove_job(job_id)
        logger.info('Job %s deleted', job_id)
    else:
        logger.warning('Failed to delete Job %s, not found', job_id)