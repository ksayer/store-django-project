from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import Category, Product


class ProductListView(generic.ListView):
    """
    List active products
    """
    model = Product
    queryset = Product.products.all()
    context_object_name = 'products'
    template_name = 'store/home.html'


class ProductDetail(generic.DetailView):
    """
    Detail information about single product
    """
    model = Product
    queryset = Product.products.all()
    context_object_name = 'product'
    template_name = 'store/products/product_detail.html'


def category_list(request, category_slug=None):
    """
    A List of products of a certain category
    """
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.products.filter(category=category)
    return render(request, 'store/products/category.html', context={'category': category, 'products': products})


class CategoryList(generic.ListView):
    model = Product
    template_name = 'store/products/category.html'
    context_object_name = 'products'

    def get_queryset(self):
        category = self.kwargs.get('category_slug', '')
        q = super().get_queryset()
        return q.filter(category=category)
