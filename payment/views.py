from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from basket.basket import Basket

@login_required
def payment_view(request):

    basket = Basket(request)
    total = str(basket.get_total_price())
    total = total.replace('.', '')
    total = int(total)
    print(total)
    stripe.api_key = 'pk_test_51K7ynJGlpPduiwahpmSEfgFnDj8f7sAeC5lMt5lHwbhZ0eYAcxQ2bCUu8bXCmlV84YLKm5qXyDIJkVeGmq1p6ejQ00Y9di8G9M'
    
    intent = stripe.PaymentIntent.create(
        amount = total,
        currency = 'gbp',
        metadata = {'userid' : request.user.id}
    )

    return render(request, 'payment/payment_info.html', {'client_secret': intent.client_secret})
