from django.contrib import admin
from costumer.models import Costumer,Employee,Bill

# Register your models here.
admin.site.register(Costumer)
admin.site.register(Employee)
admin.site.register(Bill)