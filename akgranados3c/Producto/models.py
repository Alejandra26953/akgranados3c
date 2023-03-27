from django.db import models

# Create your models here.
class Categoria(models.Model):
	categoria=models.CharField(max_length=50)
	created=models.DateTimeField(auto_now_add=True)
	updated=models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name='categoria'
		verbose_name_plural='categorias'
	def __str__(self):
		return self.categoria

class Modelo(models.Model):
	modelo=models.CharField(max_length=50)
	created=models.DateTimeField(auto_now_add=True)
	updated=models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name='Modelo'
		verbose_name_plural='Modelos'
	def __str__(self):
		return self.modelo

class Producto(models.Model):
	nombre=models.CharField(max_length=50, unique=True)
	categorias=models.ForeignKey(Categoria, on_delete=models.CASCADE)
	modelo=models.ForeignKey(Modelo, on_delete=models.CASCADE)
	imagen=models.ImageField(upload_to='computadora')
	precio=models.FloatField()
	created=models.DateTimeField(auto_now_add=True)
	updated=models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = "Producto"
		verbose_name_plural = "Productos"

	def __str__(self):
		return self.nombre
		
