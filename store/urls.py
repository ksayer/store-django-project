from django.urls import path

from . import views

app_name = 'store'

urlpatterns = [
    path('', views.ProductListView.as_view(), name='product_all'),
    path('<slug:slug>', views.ProductDetail.as_view(), name='product_detail'),
    path('shop/<slug:category_slug>', views.category_list, name='category_list'),

]