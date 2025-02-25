from django.shortcuts import render

from django.shortcuts import render

from crm_app.models import Device, DeviceInField
from crm_app.forms import SearchForm


def main_page(request):
	data = {
		"title": "crm app",
		"data": [
			{
				"button_link": "admin/",
				"title": "Заявки",
				"subtitle": "прошу, не пишите заявление",
				"overview": "Работа с заявками на оборудование",
				"img_src": "crm_app/img/zayavka2.png"
			},
			{
				"button_link": "devices/",
				"title": "Девайсы",
				"subtitle": "персОнал",
				"overview": "Работа с оборудованием",
				"img_src": "crm_app/img/personal.png"
			},
			{
				"button_link": "devpage/",
				"title": "Финансы",
				"subtitle": "за деньги да",
				"overview": "Работа с базами финансов",
				"img_src": "crm_app/img/finance.jpg"
			},
		]
	}
	return render(request, "crm_app/main_page.html", data)


def get_devices(request):
	devices = DeviceInField.objects.all()
	if request.method == 'POST':
		form = SearchForm(request.POST)

		if form.is_valid():
			search_res = []
			data_for_search = form.data['data_for_search']

			if data_for_search.isdigit():
				search_res = list(DeviceInField.objects.filter(equipment_id=int(data_for_search)))
				
			search_res = set(list(DeviceInField.objects.filter(customer__customer_name__contains=data_for_search)) + \
							 list(DeviceInField.objects.filter(equipment__manufacturer__contains=data_for_search)) + \
							 list(DeviceInField.objects.filter(equipment__model__contains=data_for_search)) + \
							 list(DeviceInField.objects.filter(owner_status__contains=data_for_search)) + search_res)

			return render(request, "crm_app/devices_page.html", {"devices": search_res, "form": form})

	return render(request, "crm_app/devices_page.html", {"devices": devices})


def zaglushka_page(request):
	return render(request, "crm_app/zaglushka_page.html", {"title": "Oops!"})