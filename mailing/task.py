from django.core.mail import send_mail
from config.settings import EMAIL_HOST_USER
from mailing.models import Mailing, TryMailing


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
