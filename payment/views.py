from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def payment_view(request):
    return render(request, 'payment/payment_info.html')
