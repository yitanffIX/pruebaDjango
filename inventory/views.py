from django.shortcuts import render, redirect
from .models import Product
from .models import Category

# Listado 

def list_products(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products':products})

def store_product(request):
    # Recuperar los datos de los input
    name = request.POST["name"]
    price = request.POST["price"]
    stock = request.POST["stock"]
    # Instanciar el nuevo objeto
    new_product = Product(name=name, price=price, stock=stock) 
    # Guardar el producto en la BD
    new_product.save()
    # Redireccionar al usuario 
    return redirect('/productos')
    
def update_product(request, id):
    # Recuperar los datos de los input
    name = request.POST["name"]
    price = request.POST["price"]
    stock = request.POST["stock"]
    # Recuperar el producto 
    product = Product.objects.get(pk=id)
    # Actualizar los campos
    product.name = name
    product.price = price
    product.stock = stock
    # Guardar los cambios en la BD
    product.save()
    # Redireccionar al usuario
    return redirect('/productos')

def delete_product(request, id):
    # Recuperar el producto
    product = Product.objects.get(pk=id)
    # Eliminarlo
    product.delete()
    # Redireccionar al usuario
    return redirect('/productos')

#Defino Categoria y listo las categorias
def list_category(request):
    categories = Category.objects.all()
    return render(request, 'category.html', {'categories':categories})

#Crear categoria
def create_category(request):
    # Recuperar los datos de los input
    name = request.POST["name"]
    description= request.POST["description"]
    #stock = request.POST["stock"]
    # Instanciar el nuevo objeto
    new_category = Category(name=name, description=description) 
    # Guardar el producto en la BD
    new_category.save()
    # Redireccionar al usuario 
    return redirect('/category')


#Actualizar las categorias
def update_category(request):
    #Recuperar los datos del input
    name = request.POST["name"]
    description = request.POST["description"]
    
    #Instanciar a la nueva categoria
    category = Category.objects.get(pk=id)
    
    category.name = name
    category.description = description
    
    # Guardar los cambios en la BD
    category.save()
    # Redireccionar al usuario
    return redirect('/category')    


#Eliminar Categoria
def delete_category(request):
    # Recuperar categoria
    category = Category.objects.get(pk=id)
    # Eliminarlo
    category.delete()
    # Redireccionar al usuario
    return redirect('/category')
