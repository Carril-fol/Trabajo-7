from django.contrib import admin
from apptp.models import Empleado, Empresa, Producto


# Register your models here.
admin.site.register(Empresa)

admin.site.register(Empleado)

admin.site.register(Producto)