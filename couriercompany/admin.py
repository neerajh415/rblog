from django.contrib import admin
from models import *



class CourierDetailsAdmin(admin.ModelAdmin):
	list_display = ('courier', 'limit', 'availability', 'preference', 'pincode')
	search_fields = ('pincode',)


admin.site.register(Citypincode)
admin.site.register(Couriercompany, CourierDetailsAdmin) 

# Register your models here.
