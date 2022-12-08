from django.shortcuts import render
from django.shortcuts import get_list_or_404
from django.http import JsonResponse
from .basket import Basket
from store.models import Product


def basket_summary(request):
    return render(request, 'store/basket/summary.html')
def basket_add(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product.id'))
        product = get_list_or_404(Product, id  = product_id)
        basket.add(product = product)
        response = JsonResponse({'test':'data'})
