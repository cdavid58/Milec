from django.db import models
from django.http import HttpResponseRedirect
from decimal import Decimal
from django.conf import settings

class Categoria(models.Model):
	nombre = models.CharField(max_length=50)

	def __str__(self):
		return self.nombre
class SubCategoria(models.Model):
	nombre = models.CharField(max_length=50)
	cat = models.ForeignKey(Categoria,on_delete=models.CASCADE)

	def __str__(self):
		return self.nombre+' | '+str(self.cat)

class SubSubCategoria(models.Model):
	nombre = models.CharField(max_length=50)
	subcategoria = models.ForeignKey(SubCategoria,on_delete=models.CASCADE)

	def __str__(self):
		return self.nombre+' | '+str(self.subcategoria)	


class Producto(models.Model):
	articulo = models.CharField(max_length=200)
	descripcion = models.TextField()
	precio = models.CharField(max_length=20)
	porcentajeOferta = models.CharField(max_length=3,default='0',null=True)
	oferta = models.BooleanField(default=False)
	agotado = models.BooleanField(default=False)
	imagen = models.ImageField(upload_to='Productos')
	subsubcategoria = models.ForeignKey(SubSubCategoria,on_delete=models.CASCADE)

	def __str__(self):
		return str(self.articulo)


class Carrito(object):
	def __init__(self,request):
		self.session = request.session
		cart = self.session.get(settings.CART_SESSION_ID)
		if not cart:
			cart = self.session[settings.CART_SESSION_ID] = {}
		self.cart = cart
		self.request = request

	def save(self):
		self.session[settings.CART_SESSION_ID]=self.cart
		self.session.modified = True

	def serializarJSON(self,producto):
		total = 0
		car = self.cart[str(producto.pk)]
		d = {'total':car['total']}
		return d

	def add(self,producto,cantidad):
		if str(producto.pk) in self.cart:
				print('Entre al if')
				#del self.cart[str(producto.pk)]
				cnt = self.cart[str(producto.pk)]
				if int(cnt['cantidad']) < int(cantidad):
					#s = int(cnt['cantidad']) + int(cantidad)
					s = int(cnt['cantidad']) + 1
					print(s,'cantidad')
					t = float(producto.precio) * float(s)
					cnt['total'] = t
					cnt['cantidad'] = s
					self.save()
				else:
					#s = int(cnt['cantidad']) - int(cantidad)
					s = int(cnt['cantidad']) - 1
					print(s,'cantidad')
					t = float(producto.precio) * float(s)
					cnt['total'] = t
					cnt['cantidad'] = s
					self.save()
		else:
			total = float(producto.precio) * float(cantidad)
			self.request.session['carrito'] += 1
			print('Entre al else que pasa')
			self.cart[str(producto.pk)] = {'codigo':producto.pk,'articulo':producto.articulo,'cantidad':cantidad,'precio':producto.precio,'total':total,'img':producto.imagen.url,
											'descripcion':producto.descripcion}
			
		print(self.cart)

	def remove(self,product):
		product_id = str(product.pk)
		if product_id in self.cart:
			del self.cart[product_id]
			self.save()

	def __iter__(self):
		product_ids = self.cart.keys()
		products = Producto.objects.filter(id__in=product_ids)
		for product in products:
			self.cart[str(product.id)]['product']=product

		for item in self.cart.values():
			item['precio']=Decimal(item['precio'])
			item['total']=item['precio']*item['cantidad']
			yield item


	def __len__(self):
		return sum(item['cantidad'] for item in self.cart.values())

	def clear(self):
		del self.session[settings.CART_SESSION_ID]
		self.session.modified = True

class Usuario(models.Model):
	nombre = models.CharField(max_length=30)
	email = models.EmailField()
	password = models.CharField(max_length=30)
	activado = models.BooleanField(default=False)
	telefono = models.CharField(max_length=10,default=1234567890)

class Datos(models.Model):
	usr = models.ForeignKey(Usuario,on_delete=models.CASCADE)
	apellido = models.CharField(max_length=30)
	direccion = models.TextField()
	calle = models.CharField(max_length=50,default=0)
	














