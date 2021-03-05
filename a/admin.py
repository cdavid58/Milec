from django.contrib import admin
from .models import *

admin.site.register(Categoria)
admin.site.register(SubCategoria)
admin.site.register(SubSubCategoria)
admin.site.register(Producto)
admin.site.register(Usuario)