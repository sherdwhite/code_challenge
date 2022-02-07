from datetime import datetime

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers import interval

from clients.models import Client
from tracking.models import SyncLog

JOB_DEFAULTS = {'max_instances': 15}
SCHEDULER = BackgroundScheduler(job_defaults=JOB_DEFAULTS)


def start_scheduler():
    print('Scheduler starting...')
    add_sync_clients_job()
    SCHEDULER.start()


def add_sync_clients_job():
    # Schedule job to be called every xx seconds
    trigger = interval.IntervalTrigger(seconds=60)
    SCHEDULER.add_job(sync_clients, trigger=trigger, id='sync_clients_job', replace_existing=True,
                      next_run_time=datetime.now())
    print('sync_clients_job added to Scheduler.')


def sync_clients():
    print('Sync Clients Start')
    now = datetime.now()
    current_minute = int(now.minute)
    # print('current_minute: {}'.format(current_minute))

    one_to_fifteen_time = current_minute % 15
    # normalize mod 15 zero value to 15
    if one_to_fifteen_time == 0:
        one_to_fifteen_time = 15
    print('mod one_to_fifteen_time time: {}'.format(one_to_fifteen_time))

    account_id_list = list(Client.objects.filter(one_to_fifteen_slot=one_to_fifteen_time).values_list('account_id',
                                                                                                      flat=True))
    print('account_id_list: {}'.format(account_id_list))

    for account_id in account_id_list:
        sync_log = SyncLog(account_id=account_id, sync_time=now)
        sync_log.save()

    print('Sync Clients End')
