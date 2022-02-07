from django.urls import include, path, re_path

from clients.views import AddClientView
from code_challenge import views
from rest_framework import routers

# template tagging
app_name = 'code_challenge'

router = routers.DefaultRouter()
router.register(r'sync_logs', views.SyncLogViewSet)

urlpatterns = [
    re_path(r'^$', views.ResultsView.as_view(), name='index'),
    path('add_client', AddClientView.as_view(), name='add_client'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
