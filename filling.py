import codecs
import django
from blog.models import Shops, Products, Manufactures, ShopsAndProducts, ProductsAndManufactures

f = codecs.open('data/manufactures.txt', 'r', 'UTF-8')
line = f.readline()
lines = f.readlines()
for line in lines:
    mas = line.split('\t')
    ma = Manufactures()
    ma.id = mas[0]
    ma.name = mas[1]
    ma.telephone = mas[2]
    ma.save()
f.close()

f = codecs.open('data/shops.txt', 'r', 'UTF-8')
line = f.readline()
lines = f.readlines()
for line in lines:
    mas = line.split('\t')
    ma = Shops()
    ma.id = mas[0]
    ma.name = mas[1]
    ma.address =f.close mas[2]
    ma.save()
f.close()

f = codecs.open('data/products.txt', 'r', 'UTF-8')
line = f.readline()
lines = f.readlines()
for line in lines:
    mas = line.split('\t')
    ma = Products()
    ma.id = mas[0]
    ma.name = mas[1]
    ma.price = mas[2]
    ma.save()
f.close()


f = codecs.open('data/products_and_manufactures.txt', 'r', 'UTF-8')
line = f.readline()
lines = f.readlines()
for line in lines:
    mas = line.split('\t')
    p = Products.objects.get(id = mas[0])
    m = Manufactures.objects.get(id = mas[1])
    ProductsAndManufactures.objects.create(date = "2018-05-01", product = p, manufacture = m)
f.close()

f = codecs.open('data/shops_and_products.txt', 'r', 'UTF-8')
line = f.readline()
lines = f.readlines()
for line in lines:
    mas = line.split('\t')
    s = Shops.objects.get(id = mas[0])
    p = Products.objects.get(id = mas[1])  
    ShopsAndProducts.objects.create(count = 100, product = p, shop = s)
f.close()
