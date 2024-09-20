from datetime import datetime, timedelta

from django.core.mail import send_mail
from config.settings import EMAIL_HOST_USER
from mailing.models import Mailing, TryMailing


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


def select_mailings():
    mailing_list = Mailing.objects.filter(next_send_date__isnull=True)
    for i in mailing_list:
        i.next_send_date = i.send_date
        i.save()

    today = datetime.today()

    mailing_list = Mailing.objects.filter(next_send_date=today)

    for mailing in mailing_list:
        emails_list = mailing.client.filter(is_active=True).values_list('email', flat=True)
        if send_mail(
            subject=mailing.message.title,
            message=mailing.message.body,
            from_email=EMAIL_HOST_USER,
            recipient_list=emails_list,
            fail_silently=False):
            TryMailing.objects.create(mailing=mailing, status='success', response='Сообщение доставлено')
        else:
            TryMailing.objects.create(mailing=mailing, status='fail', response='Сообщение не доставлено')

        if mailing.interval == Mailing.DAY:
            diff = 1
        elif mailing.interval == Mailing.WEEK:
            diff = 7
        else:
            diff = 30
        mailing.next_send_date = mailing.next_send_date + timedelta(days=diff)
        mailing.save()
