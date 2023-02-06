from django.views.generic import ListView, DetailView
from .models import Device
from django.urls import reverse_lazy

# Create your views here.


class DeviceListView(ListView):
    model = Device
    template_name = 'device_list.html'


class DeviceDetailView(DetailView):
    model = Device
    template_name = 'device_detail.html'
