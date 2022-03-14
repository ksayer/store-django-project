from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404

from store.models import Product
from .basket import Basket


def basket_summary(request):
    # basket = Basket(request)  # Можно убрать, т.к. есть такой же контекст процессор
    return render(request, 'store/basket/summary.html')


def basket_add(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        product = get_object_or_404(Product, id=product_id)
        basket.add(product=product, qty=product_qty)

        basketqty = basket.__len__()
        print(basketqty)
        print(basket.__dict__)
        response = JsonResponse({'qty': basketqty})

        return response
