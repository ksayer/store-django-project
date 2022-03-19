from django.contrib.auth.decorators import login_required

from django.shortcuts import render
from .models import Order, OrderItem
from account.models import UserBase
from .forms import PaymentForm
from basket.basket import Basket


def order_placed(request):
    """
    Create order
    """
    basket = Basket(request)
    user = UserBase.objects.get(id=request.user.id)
    form = PaymentForm(request.POST)
    if form.is_valid():
        form.cleaned_data['user'] = user
        form.cleaned_data['total_paid'] = basket.get_total_price()
        order = Order.objects.create(**form.cleaned_data)
        for item in basket:
            OrderItem.objects.create(order=order, product=item['product'],
                                     price=item['price'], quantity=item['qty'])
        basket.clear()
    return render(request, 'orders/order_placed.html')


@login_required
def payment(request):
    """
    Payment
    """
    form = PaymentForm()
    return render(request, 'orders/payment.html', context={'form': form})
