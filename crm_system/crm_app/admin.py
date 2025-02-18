from django.contrib import admin

from .models import Device, DeviceInField, Customer, Order

admin.site.register(Device)
admin.site.register(DeviceInField)
admin.site.register(Customer)
admin.site.register(Order)