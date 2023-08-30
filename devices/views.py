from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Device
from django.urls import reverse_lazy

# Create your views here.


class DeviceListView(ListView):
    model = Device
    template_name = 'device_list.html'


class DeviceDetailView(DetailView):
    def get(self, request, slug):
        device = Device.objects.get(url=slug)
        return render(request, "device_detail.html", {"device": device})
    # model = Device
    # template_name = 'device_detail.html'

