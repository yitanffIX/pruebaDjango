from django.contrib import admin
from django.urls import path
from inventory.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('productos/', list_products, name='list_product'),
    path('guardar/producto/', store_product, name="store_product"),
    path('actualizar/producto/<id>', update_product , name="update_product"),
    path('eliminar/producto/<id>', delete_product, name="delete_product"),
]
