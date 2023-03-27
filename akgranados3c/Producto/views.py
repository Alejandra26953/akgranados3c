from django.shortcuts import render, HttpResponse, redirect
from .models import Producto
# Create your views here.

def producto_list(request):

	tienda = Producto.objects.all()

	return render(request, "product.html", {"ferre": tienda})

