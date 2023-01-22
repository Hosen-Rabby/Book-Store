from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import stripe
from basket.basket import Basket

@login_required
def payment_view(request):

    basket = Basket(request)
    total = str(basket.get_total_price())
    total = total.replace('.', '')
    total = int(total)
    print(total)
    print(555)
    stripe.api_key = 'sk_test_51K7ynJGlpPduiwahiUaCtLBMeDpIIqxVRhugecNbRGmBzFDMuA4khyDmzMM0uUcsjZKRL0mWQhBqCnFB5Wqvg3dF00aVIkritV'
    
    intent = stripe.PaymentIntent.create(
        amount = total,
        currency = 'gbp',
        metadata = {'userid' : request.user.id}
    )

    return render(request, 'payment/payment_info.html', {'client_secret': intent.client_secret})
    print(intent)
    print('---',3)
# Consolas, 'Courier New', monospace