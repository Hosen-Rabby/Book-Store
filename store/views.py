from django.shortcuts import render, get_object_or_404
from .models import Category, Product

def all_products(request):
    products = Product.objects.all()
    size = len(products)
    return render(request, 'store/home.html', {'products':products, 'size':size})

    # print('products')
    # categories = Category.objects.all()

def prod_details(request, slug):
    product = get_object_or_404(Product, slug = slug, in_stock = True)
    # prod_details = Product.objects.all()
    return render(request, 'store/single_prod.html', {'product':product})


def category_list(request, category_slug):
    category = get_object_or_404(Category, slug = category_slug)
    products = Product.objects.filter(category = category)
    size = len(products)
    return render(request, 'store/category.html', {'products':products, 'category':category, 'size':size})


