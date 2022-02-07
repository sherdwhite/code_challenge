from rest_framework import serializers

from tracking.models import SyncLog


class SyncSerializer(serializers.ModelSerializer):
    class Meta:
        model = SyncLog
        fields = ['account_id', 'sync_time']
