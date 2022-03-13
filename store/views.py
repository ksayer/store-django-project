from django.shortcuts import render, get_object_or_404

from .models import Category, Product


def product_all(request):
    products = Product.products.all()
    return render(request, 'store/home.html', context={'products': products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'store/products/product_detail.html', context={'product': product})


def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.products.filter(category=category)
    return render(request, 'store/products/category.html', context={'category': category, 'products': products})
