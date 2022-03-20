from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('payment/', views.payment, name='payment'),
]