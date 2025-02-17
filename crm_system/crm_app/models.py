from django.db import models

class Device(models.Model):
	''' Модель оборудования '''
	
	class Meta:
		db_table = "devices_model"
		verbose_name = "доступное оборудование"
		verbose_name_plural = "доступное оборудование"
		
	manufacturer = models.CharField(verbose_name="производитель")
	model = models.CharField(verbose_name="модель")
	
	def __str__(self):
		return f"{self.model} от {self.manufacturer}"
		
class Customer(models.Model):
	''' Заказчики '''
	
	class Meta:
		db_table = "customer"
		verbose_name = "заказчик"
		verbose_name_plural = "заказчик"
		
	customer_name = models.CharField(verbose_name="название компании заказчика")
	customer_address = models.CharField(verbose_name="полный адрес компании заказчика")
	customer_city = models.CharField(verbose_name="город компании заказчика")
	
	def __str__(self):
		return self.customer_name
		
class DeviceInField(models.Model):
	''' Оборудование в полях '''
	
	class Meta:
		db_table = "device_in_field"
		verbose_name = "оборудование в полях"
		verbose_name_plural = "оборудование в полях"
		
	serial_number = models.CharField(verbose_name="серийный номер")
	owner_status = models.CharField(verbose_name="статус заказа")
	customer = models.ForeignKey(Customer, on_delete=models.RESTRICT, verbose_name="идентификатор пользователя")
	equipment = models.ForeignKey(Device, on_delete=models.RESTRICT, verbose_name="идентификатор оборудования")