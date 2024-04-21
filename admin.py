# gas_services/admin.py

from django.contrib import admin
from .models import Customer, Bill, MeterReading

admin.site.register(Customer)
admin.site.register(Bill)
admin.site.register(MeterReading)
