from django.urls import path

from .views import DeviceListView, DeviceDetailView

from .views import DeviceListView
urlpatterns = [
    path('', DeviceListView.as_view(), name='device_list'),
    path('<int:pk>/', DeviceDetailView.as_view(), name='device_detail')
]