from django.contrib import admin
from .models import Categoria, Producto, Modelo

# Register your models here.
class CategoriaprodAdmin(admin.ModelAdmin):
	readonly_fields=("created","updated")

class ProductoAdmin(admin.ModelAdmin):
	readonly_fields=("created","updated")

class ModeloAdmin(admin.ModelAdmin):
	readonly_fields=("created","updated")

admin.site.register(Categoria, CategoriaprodAdmin)

admin.site.register(Producto, ProductoAdmin)

admin.site.register(Modelo , ModeloAdmin )
