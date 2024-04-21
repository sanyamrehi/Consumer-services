# gas_services/models.py

from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()

class Bill(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField()

class MeterReading(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    reading_date = models.DateField()
    reading = models.DecimalField(max_digits=10, decimal_places=2)
