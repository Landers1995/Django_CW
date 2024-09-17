from django.core.mail import send_mail
from config.settings import EMAIL_HOST_USER
from mailing.models import Mailing, TryMailing, Client

import logging
from django.conf import settings
from apscheduler.schedulers.background import BackgroundScheduler, BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django.core.management.base import BaseCommand
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution
from django_apscheduler import util
from django.core.management import BaseCommand
#from mailing.task import send_mailing
from mailing.utils import get_mailing_period_trigger


def send_mailing():
    mailings = Mailing.objects.filter(is_active=True)

    for mailing in mailings:
        emails_list = mailing.client.filter(is_active=True).values_list('email', flat=True)
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


def send_mailing_plural():
    scheduler = BackgroundScheduler(timezone=settings.TIME_ZONE)
    scheduler.add_jobstore(DjangoJobStore(), "default")
    mailing = Mailing()
    trigger = get_mailing_period_trigger(mailing.pk)

    scheduler.add_job(
        send_mailing,
        trigger=trigger,
        id="send_mailing",
        max_instances=1,
        replace_existing=True,
        )

    try:
        scheduler.start()
    except KeyboardInterrupt:
        scheduler.shutdown()
