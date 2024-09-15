from apscheduler.triggers.cron import CronTrigger

from mailing.models import Mailing


def get_mailing_period_trigger(mailing: Mailing) -> CronTrigger:
    start_date = mailing.send_date

    if mailing.interval == Mailing.interval.MINUTE:
        trigger = CronTrigger(second='*/10', start_date=start_date)
    elif mailing.interval == Mailing.interval.DAY:
        trigger = CronTrigger(second='*/59', start_date=start_date)
        #     day='*', hour=start_date.hour, minute=start_date.minute, start_date=start_date
        # )
    elif mailing.interval == Mailing.interval.WEEK:
        trigger = CronTrigger(
            day_of_week=start_date.weekday(),
            hour=start_date.hour,
            minute=start_date.minute,
            start_date=start_date,
        )
    elif mailing.interval == Mailing.interval.MONTH:
        trigger = CronTrigger(
            month='*',
            day=start_date.day,
            hour=start_date.hour,
            minute=start_date.minute,
            start_date=start_date,
        )
    else:
        raise NotImplementedError

    return trigger
