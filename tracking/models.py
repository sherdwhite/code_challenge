from django.db.models import IntegerField, DateTimeField
from model_utils.models import TimeStampedModel


class SyncLog(TimeStampedModel):
    account_id = IntegerField()
    sync_time = DateTimeField()
