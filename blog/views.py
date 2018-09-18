from django.shortcuts import render
from django.utils import timezone
from .models import Post, Shops, Products, Manufactures, ShopsAndProducts, ProductsAndManufactures
from django.shortcuts import render, get_object_or_404
from .forms import PostForm, FindProductForm, FindShopForm, FindManufactureForm
from django.shortcuts import redirect


def shop_list(request):
    shops = Shops.objects.all()
    return render(request, 'blog/shop_list.html', {'shops': shops})


def product_list(request, pk):
    products = list(Products.objects.filter(shopsandproducts__shop_id=pk).order_by('name'))
    return render(request, 'blog/product_list.html', {'products': products, 'pk': pk})


def product(request, pk1, pk2):
    product = Products.objects.get(id = pk2)
    count = ShopsAndProducts.objects.get(shop_id = pk1, product_id = pk2).count
    date = ProductsAndManufactures.objects.get(product_id = pk2).date
    manufacture = Manufactures.objects.get(productsandmanufactures__product_id = pk2)
    return render(request, 'blog/product.html', {'product': product, 'manufacture': manufacture, 'date': date, 'count': count})


def manufacture(request, pk):
    manufacture = Manufactures.objects.get(id = pk)
    return render(request, 'blog/manufacture.html', {'manufacture': manufacture})





def filter(request):
    return render(request, 'blog/filter.html')


def findproduct(request):
    if request.method == "POST":
        form = FindProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False) 
            products = Products.objects.filter(name = product.name)
            return render(request, 'blog/f_product_list.html', {'products': products})
    else:
        form = FindProductForm()
        return render(request, 'blog/findproduct.html', {'form': form})


def addresses(request, pk):
    product = Products.objects.get(id=pk)
    shops = Shops.objects.filter(shopsandproducts__product_id=pk)
    l = len(shops)
    return render(request, 'blog/addresses.html', {'product': product, 'shops': shops, 'l': l})


def findshop(request):
    if request.method == "POST":
        form = FindShopForm(request.POST)
        if form.is_valid():           
            shop = form.save(commit=False) 
            shops = Shops.objects.filter(name = shop.name)
            return render(request, 'blog/f_shop_list.html', {'shops': shops})
    else:
        form = FindShopForm()
        return render(request, 'blog/findshop.html', {'form': form})


def products(request, pk):
    shop = Shops.objects.get(id=pk)
    products = Products.objects.filter(shopsandproducts__shop_id=pk)
    l = len(products)
    return render(request, 'blog/products.html', {'products': products, 'shop': shop, 'l': l})


def findmanufacture(request):
    if request.method == "POST":
        form = FindManufactureForm(request.POST)
        if form.is_valid():
            manufac = form.save(commit=False) 
            manufacture = Manufactures.objects.get(name = manufac.name)
            products = Products.objects.filter(productsandmanufactures__manufacture_id = manufacture.id)
            l = len(products)
            return render(request, 'blog/f_manufacture.html', {'manufacture': manufacture, 'products': products, 'l': l})
    else:
        form = FindManufactureForm()
        return render(request, 'blog/findmanufacture.html', {'form': form})





