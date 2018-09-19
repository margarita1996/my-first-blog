from django.shortcuts import render
from django.utils import timezone
from .models import Post, Shops, Products, Manufactures, ShopsAndProducts, ProductsAndManufactures
from django.shortcuts import render, get_object_or_404
from .forms import PostForm, FindProductForm, FindShopsForm, FindShopForm, FindManufactureForm, FindPriceForm
from django.shortcuts import redirect


def shop_list(request):
    shops = Shops.objects.all()
    return render(request, 'blog/shop_list.html', {'shops': shops})


def product_list(request, pk):
    shop = Shops.objects.get(id = pk)
    products = Products.objects.filter(shopsandproducts__shop_id=pk).order_by('name')
    l = len(products)
    return render(request, 'blog/product_list.html', {'products': products, 'shop': shop, 'pk': pk, 'l': l})


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
            l = len(products)
            if l == 0:
                return render(request, 'blog/exception.html', {'e': 4})
            return render(request, 'blog/f_product_list.html', {'products': products})
    else:
        form = FindProductForm()
        return render(request, 'blog/findproduct.html', {'form': form})


def addresses(request, pk):
    product = Products.objects.get(id=pk)
    shops = Shops.objects.filter(shopsandproducts__product_id=pk)
    l = len(shops)
    return render(request, 'blog/addresses.html', {'product': product, 'shops': shops, 'l': l})


def findshops(request):
    if request.method == "POST":
        form = FindShopsForm(request.POST)
        if form.is_valid():           
            shop = form.save(commit=False) 
            shops = Shops.objects.filter(name = shop.name)
            l = len(shops)
            if l == 0:
                return render(request, 'blog/exception.html', {'e': 3})
            return render(request, 'blog/f_shop_list.html', {'shops': shops})
    else:
        form = FindShopsForm()
        return render(request, 'blog/findshops.html', {'form': form})


def products(request, pk):
    shop = Shops.objects.get(id=pk)
    products = Products.objects.filter(shopsandproducts__shop_id=pk)
    l = len(products)
    return render(request, 'blog/products.html', {'products': products, 'shop': shop, 'l': l})


def findshop(request):
    if request.method == "POST":
        form = FindShopForm(request.POST)
        if form.is_valid():           
            sh = form.save(commit=False) 
            shops = Shops.objects.filter(address = sh.address)
            l = len(shops)
            if l == 0:
                return render(request, 'blog/exception.html', {'e': 2})
            shop = shops[0]
            products = Products.objects.filter(shopsandproducts__shop_id=shop.id)
            l = len(products)
            return render(request, 'blog/products.html', {'products': products, 'shop': shop, 'l': l})
    else:
        form = FindShopForm()
        return render(request, 'blog/findshop.html', {'form': form})


def findmanufacture(request):
    if request.method == "POST":
        form = FindManufactureForm(request.POST)
        if form.is_valid():
            manufac = form.save(commit=False) 
            manufactures = list(Manufactures.objects.filter(name = manufac.name))
            l = len(manufactures)
            if l == 0:
                return render(request, 'blog/exception.html', {'e': 1})
            manufacture = manufacture[0]
            products = Products.objects.filter(productsandmanufactures__manufacture_id = manufacture.id)
            lp = len(products)
            return render(request, 'blog/f_manufacture.html', {'manufacture': manufacture, 'products': products, 'lp': lp, 'lm':lm})
    else:
        form = FindManufactureForm()
        return render(request, 'blog/findmanufacture.html', {'form': form})


def findprice(request):
    if request.method == "POST":
        form = FindPriceForm(request.POST)
        if (form.is_valid()):
            product = form.save(commit=False) 
            products = Products.objects.filter(price = product.price)
            l = len(products)
            if l == 0:
                return render(request, 'blog/exception.html', {'e': 5})
            return render(request, 'blog/f_product_list.html', {'products': products})
    else:
        form = FindPriceForm()
        return render(request, 'blog/findprice.html', {'form': form})





