from django.core.mail import send_mail
from config.settings import EMAIL_HOST_USER
from mailing.models import Mailing, TryMailing

import logging
from django.conf import settings
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django.core.management.base import BaseCommand
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution
from django_apscheduler import util
from django.core.management import BaseCommand
#from mailing.task import send_mailing


def send_mailing():
    mailings = Mailing.objects.filter(is_active=True)

    for mailing in mailings:
        emails_list = mailing.client.values_list('email', flat=True)
        try:
            send_mail(
                subject=mailing.message.title,
                message=mailing.message.body,
                from_email=EMAIL_HOST_USER,
                recipient_list=emails_list
            )
        except Exception as e:
            TryMailing.objects.create(mailing=mailing, error=e, status='fail', response='Сообщение не доставлено')
        else:
            TryMailing.objects.create(mailing=mailing, status='success', response='Сообщение доставлено')

 # def send_mailing_plural():
 #        scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
 #        scheduler.add_jobstore(DjangoJobStore(), "default")
 #
 #        scheduler.add_job(
 #            send_mailing,
 #            trigger=CronTrigger(second="*/59"),  # Every 10 seconds
 #            id="send_mailing",  # The `id` assigned to each job MUST be unique
 #            max_instances=1,
 #            replace_existing=True,
 #        )
 #
 #        try:
 #            #logger.info("Starting scheduler...")
 #            #TryMailing.objects.create(mailing=mailing, error=e, status='fail', response='Сообщение не доставлено')
 #            scheduler.start()
 #        except KeyboardInterrupt:
 #            #logger.info("Stopping scheduler...")
 #            scheduler.shutdown()
 #            #logger.info("Scheduler shut down successfully!")