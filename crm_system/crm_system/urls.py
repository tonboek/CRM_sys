from django.contrib import admin
from django.urls import path, include
import crm_app.views

urlpatterns = [
	path('admin/', admin.site.urls),
	path('crm_app/', include('crm_app.urls')),
	path('', crm_app.views.main_page, name='main_page'),
	path('devices/', crm_app.views.get_devices, name='get_devices'),
	path('devpage/', crm_app.views.zaglushka_page, name='zaglushka_page')
]
