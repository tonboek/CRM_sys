from django.contrib import admin

from .models import Device, DeviceInField, Customer, Order

class DeviceAdmin(admin.ModelAdmin):
	list_display = ('id', 'manufacturer', 'model')
	search_fields=('manufacturer', 'model')
	
class CustomerAdmin(admin.ModelAdmin):
	list_display = ('id', 'customer_name', 'customer_address', 'customer_city')
	search_fields=('customer_name', 'customer_address')
	
class OrderAdmin(admin.ModelAdmin):
	def my_customer(self, obj):
		return obj.device.customer.customer_name
	def my_serial_number(self, obj):
		return obj.device.serial_number
	def my_device_model(self, obj):
		return obj.device.equipment.model
	def my_device_manufacturer(self, obj):
		return obj.device.equipment.manufacturer
		
	my_customer.short_description = 'пользователь'
	my_serial_number.short_description = 'серийный номер'
	my_device_model.short_description = 'модель'
	my_device_manufacturer.short_description = 'производитель'
	
	list_display=('id', 'my_device_manufacturer', 'my_device_model', 'my_serial_number', my_customer)
	search_fields=('device__customer__customer_name', 'device__id', 'device__serial_number', 'device__equipment__model', 'device__equipment__manufacturer')
	raw_id_fields=('device', 'customer')
	
class DeviceInFieldAdmin(admin.ModelAdmin):
	def my_customer(self, obj):
		return obj.customer.customer_name
	def my_device_model(self, obj):
		return obj.equipment.model
	def my_device_manufacturer(self, obj):
		return obj.equipment.manufacturer
		
	my_customer.short_description = 'пользователь'
	my_device_model.short_description = 'модель'
	my_device_manufacturer.short_description = 'производитель'
	
	list_display = ('id', 'my_device_manufacturer', 'my_device_model')
	search_fields=('serial_number', 'equipment__manufacturer', 'equipment__model')
	raw_id_fields=('customer', 'equipment')

admin.site.register(Device, DeviceAdmin)
admin.site.register(DeviceInField, DeviceInFieldAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order, OrderAdmin)