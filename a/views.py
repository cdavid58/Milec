from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .email import *
import json

def home(request):
	if "carrito" in request.session:
		print('SI EXISTE')
	else:
		carrito = request.session['carrito'] = 0

	cat = Categoria.objects.all()
	subCat = SubCategoria.objects.all()
	subSubCat = SubSubCategoria.objects.all()
	producto = Producto.objects.filter(agotado = False,oferta=False)
	return render(request,'index.html',{'p':producto, 'cat':cat,'subCat':subCat,
					'subSubCat':subSubCat,
					'carrito':request.session['carrito']
		})

def categoria(request,pk):
	subCat = SubSubCategoria.objects.get(pk=pk)
	producto = Producto.objects.filter(agotado=False,oferta=False,subsubcategoria=subCat)

	if request.is_ajax():
		print(request.GET.get('product'))
		cart_add(request,request.GET.get('product'),1)
		return HttpResponse(request.session['carrito'])

	cat = Categoria.objects.all()
	subCate = SubCategoria.objects.all()
	subSubCat = SubSubCategoria.objects.all()

	return render(request,'categoria.html',{'p':producto,
					'cat':cat,'subCate':subCate,
					'subSubCat':subSubCat,
					'carrito':request.session['carrito'],'pk':pk
				})



def detailProduct(request,pk):
	producto = Producto.objects.get(pk=pk)

	cat = Categoria.objects.all()
	subCate = SubCategoria.objects.all()
	subSubCat = SubSubCategoria.objects.all()

	if request.is_ajax():
		print(request.GET.get('product'))
		cart_add(request,request.GET.get('product'),1)
		return HttpResponse(request.session['carrito'])


	return render(request,'detail.html',{'p':producto,
						'cat':cat,'subCat':subCate,
						'subSubCat':subSubCat,
						'carrito':request.session['carrito'],'pk':pk
					})	


def cart_remove(request,product_id):
	cart = Carrito(request)
	product = Producto.objects.get(pk=product_id)
	cart.remove(product)
	resta = int(request.session['carrito']) - 1
	request.session['carrito'] = resta
	return redirect('carritoShop')

def carritoShop(request):

	if request.is_ajax():
		if request.GET.get('delete') is not None:
			print(request.GET.get('delete'))
			cart_remove(request,int(request.GET.get('delete')))
		else:
			cart_add(request,request.GET.get('pro'),request.GET.get('cant'))
			cart = Carrito(request)
			producto = Producto.objects.get(pk=request.GET.get('pro'))
			return HttpResponse(json.dumps(cart.serializarJSON(producto)))


	cart = Carrito(request)
	total = 0
	for i in cart:
		total += i['total']

	totalConEnvio = total + 10

	cat = Categoria.objects.all()
	subCate = SubCategoria.objects.all()
	subSubCat = SubSubCategoria.objects.all()
	return render(request,'carrito.html',{'carrito':request.session['carrito'],'cat':cat,'subCat':subCate,
						'subSubCat':subSubCat,
						'cart':cart,'total':total,'totalConEnvio':totalConEnvio
				})


def datos(request):
	cart = Carrito(request)
	if len(cart) > 0:
		if 'usuario' in request.session:
			usr = Usuario.objects.get(email=request.session['usuario'])
			if usr.activado:
				try:
					d = Datos.objects.get(usr=usr)
				except Datos.DoesNotExists:
					d = None
				if d is not None:
					return redirect('methodPago')
				else:

					if request.method == 'POST':
						Datos(
							usr = usr,
							apellido = request.POST.get('apellido'),
							direccion = request.POST.get('dir'),
							calle = request.POST.get('calle')
						).save()
						return redirect('methodPago')

					cat = Categoria.objects.all()
					subCate = SubCategoria.objects.all()
					subSubCat = SubSubCategoria.objects.all()
					cart = Carrito(request)
					total = 0
					for i in cart:
						total += i['total']

					totalConEnvio = total + 10
					return render(request,'checkout.html',{'carrito':request.session['carrito'],'cat':cat,'subCat':subCate,
										'subSubCat':subSubCat,'total':total,'totalConEnvio':totalConEnvio,
										'nombre':usr.nombre,'tlf':usr.telefono,'email':usr.email					
								})
			return redirect('/')
		return redirect('/')
	return redirect('carritoShop')


def methodPago(request):

	if request.method == 'POST':
		return redirect('revisa')

	cat = Categoria.objects.all()
	subCate = SubCategoria.objects.all()
	subSubCat = SubSubCategoria.objects.all()
	cart = Carrito(request)
	total = 0
	for i in cart:
		total += i['total']

	totalConEnvio = total + 10
	return render(request,'checkout2.html',{
		'carrito':request.session['carrito'],'cat':cat,'subCat':subCate,
		'subSubCat':subSubCat,'total':total,'totalConEnvio':totalConEnvio
		})


def revisa(request):
	if request.method == 'POST':
		return redirect('invoice')
	cat = Categoria.objects.all()
	subCate = SubCategoria.objects.all()
	subSubCat = SubSubCategoria.objects.all()
	cart = Carrito(request)
	total = 0
	for i in cart:
		total += i['total']

	totalConEnvio = total + 10

	return render(request,'checkout3.html',{
		'carrito':request.session['carrito'],'cat':cat,'subCat':subCate,
		'subSubCat':subSubCat,'total':total,'totalConEnvio':totalConEnvio,'cart':cart
		})

def invoice(request):

	cat = Categoria.objects.all()
	subCate = SubCategoria.objects.all()
	subSubCat = SubSubCategoria.objects.all()
	cart = Carrito(request)
	total = 0
	for i in cart:
		total += i['total']

	totalConEnvio = total + 10
	cartt = cart
	cart.clear()
	request.session['carrito'] = 0
	return render(request,'invoice.html',{
		'carrito':request.session['carrito'],'cat':cat,'subCat':subCate,
		'subSubCat':subSubCat,'total':total,'totalConEnvio':totalConEnvio,'cart':cartt
		})

#############################################################################################
# ACCIONES DEL CARRITO

def cart_add(request,product_id,cantidad):
	producto = Producto.objects.get(pk=product_id)
	cart = Carrito(request)
	cart.add(producto,int(cantidad))




def registro(request):
	if request.method == 'POST':
		Usuario(
			nombre = request.POST.get('name'),
			email = request.POST.get('email'),
			password = request.POST.get('pass'),
			telefono = request.POST.get('tlf')
		).save()
		activacion(request,request.POST.get('name'),request.POST.get('email'),request.POST.get('pass'),request.POST.get('tlf'))
		return thanks(request,request.POST.get('email'))

	cat = Categoria.objects.all()
	subCate = SubCategoria.objects.all()
	subSubCat = SubSubCategoria.objects.all()
	return render(request,'register.html',{'carrito':request.session['carrito'],'cat':cat,'subCat':subCate,
						'subSubCat':subSubCat})


def thanks(request,email):
	return render(request,'thanks.html',{'email':email})

def activacionCuenta(request,tlf):
	usr = Usuario.objects.get(telefono=tlf)
	usr.activado = True
	usr.save()
	request.session['usuario'] = usr.email
	cart = Carrito(request)
	if len(cart) > 0:
		return redirect('carritoShop')
	return redirect('/')

def login(request):
	if request.method == 'POST':
		try:
			usr = Usuario.objects.get(email = request.POST.get('email'), password=request.POST.get('pass'))
		except Usuario.DoesNotExists:
			usr = None
		cart = Carrito(request)
		if usr is not None:
			request.session['usuario'] = usr.email
			if len(cart) > 0:
				return redirect('carritoShop')
			else:
				return redirect('/')
	return render(request,'register.html')




























