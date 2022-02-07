from django.views.generic import ListView
from rest_framework import viewsets

from code_challenge.serializers import SyncSerializer
from tracking.models import SyncLog


class ResultsView(ListView):
    context_object_name = 'sync_logs'
    model = SyncLog
    ordering = ['-modified']
    template_name = 'code_challenge/results.html'

    def __init__(self):
        super().__init__()
        self.object_list = self.model.objects.all()

    def get_queryset(self):
        sync_logs = SyncLog.objects.all().order_by('-modified')[:1000]
        return sync_logs


class SyncLogViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Sync Logs to be viewed.
    """
    queryset = SyncLog.objects.all().order_by('-modified')
    serializer_class = SyncSerializer
