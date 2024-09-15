# import logging
#
# from django.conf import settings
# from django_apscheduler.util import close_old_connections
#
# from mailing.models import Mailing
# from mailing.tg import send_tg_message
#
# logger = logging.getLogger(__name__)
#
#
# # @close_old_connections
# def schedule_mailing(mailing_id: int) -> None:
#     mailing = Mailing.objects.get(id=mailing_id)
#     mailing.status = Mailing.Status.RUNNING
#     mailing.save()
#
#     send_tg_message(settings.TG_CHAT_ID, f'Mailin {mailing.id} has been send')
#     logger.info('Message about mailing %d was sent', mailing_id)
#
#     mailing.status = Mailing.Status.FINISHED