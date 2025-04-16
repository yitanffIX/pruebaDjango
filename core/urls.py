from django.contrib import admin
from django.urls import path
from inventory.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('productos/', list_products, name='list_product'),
    path('guardar/producto/', store_product, name="store_product"),
    path('actualizar/producto/<id>', update_product , name="update_product"),
    path('eliminar/producto/<id>', delete_product, name="delete_product"),
    path('categories/', list_category, name='list_category'),
    path('guardar/category/', crate_category, name='create_category'),
    path('actualizar/category/<id>', update_category, name='update_category'),
    path('eliminar/category//<id>', delete_category, name='delete_category'),
]
