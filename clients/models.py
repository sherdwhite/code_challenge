from django.db.models import CharField, IntegerField
from model_utils.models import TimeStampedModel


class Client(TimeStampedModel):
    account_id = IntegerField(unique=True, db_index=True)
    one_to_fifteen_slot = IntegerField(null=True, blank=True)
