from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^$',home,name='home'),
    url(r'^categoria/(\d+)/$',categoria,name="categoria"),

    url(r'^detail/(\d+)/$',detailProduct,name='detailProduct'),

    url(r'^register/$',registro,name="registro"),
    url(r'^login/$',login,name="login"),

    url(r'^activacion/(\w+)/$',activacionCuenta,name="activacionCuenta"),

    ###########################################################
    # ACCIONES CARRITO

    url(r'^shoppingcart/$',carritoShop,name='carritoShop'),


    url(r'^checkout/$',datos,name="datos"),
    url(r'^methodPago/$',methodPago,name="methodPago"),
    url(r'^revisa/$',revisa,name="revisa"),

    url(r'^invoice/$',invoice,name="invoice"),

   ]