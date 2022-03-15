from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from store.models import Product
from .basket import Basket


def basket_summary(request):
    # basket = Basket(request)
    return render(request, 'store/basket/summary.html')


def basket_add(request):
    """
    Add product to session using ajax
    """
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        product = get_object_or_404(Product, id=product_id)
        basket.add(product=product, qty=product_qty)

        basketqty = basket.__len__()
        response = JsonResponse({'qty': basketqty})

        return response


def basket_delete(request):
    """
    Delete product from session usig ajax
    """
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = request.POST.get('productid')
        print('id', product_id)
        basket.delete(product_id=product_id)
        response = JsonResponse({'Success': True})
        return response
