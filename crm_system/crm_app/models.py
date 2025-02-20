from django.db import models

STATUSES = [
		("O", "открытa"),
		("C", "закрытa"),
		("IP", "в процессе"),
		("NI", "нужна информация"),
	]

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
		return f"{self.customer_name} по адресу {self.customer_address}"
		
class DeviceInField(models.Model):
	''' Оборудование в полях '''
	
	class Meta:
		db_table = "device_in_field"
		verbose_name = "оборудование в полях"
		verbose_name_plural = "оборудование в полях"
		
	serial_number = models.CharField(verbose_name="серийный номер")
	owner_status = models.CharField(verbose_name="статус заказа", choices=STATUSES)
	customer = models.ForeignKey(Customer, on_delete=models.RESTRICT, verbose_name="идентификатор пользователя")
	equipment = models.ForeignKey(Device, on_delete=models.RESTRICT, verbose_name="идентификатор оборудования")
	
	def __str__(self):
		return f"{self.equipment} с/н {self.serial_number} в {self.customer}"
	
class Order(models.Model):
	''' описание заявки '''
	
	class Meta:
		db_table = 'order'
		verbose_name = 'заявки'
		verbose_name_plural = 'заявки'
		
	device = models.ForeignKey(DeviceInField, verbose_name='оборудование', on_delete=models.RESTRICT)
	customer = models.ForeignKey(Customer, verbose_name='заказчик', on_delete=models.RESTRICT)
	order_description = models.CharField(verbose_name='описание заявки')
	created_at = models.DateTimeField(verbose_name='создано в', auto_now_add=True)
	updated_at = models.DateTimeField(verbose_name='последнее изменение', auto_now=True)
	order_status = models.CharField(verbose_name='статус заявки', choices=STATUSES)

	def __str__(self):
		return f"заказ №{self.id} для {self.device}"