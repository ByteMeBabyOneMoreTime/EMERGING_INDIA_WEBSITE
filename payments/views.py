import razorpay
from django.shortcuts import render, redirect
from django.conf import settings
from .models import payment, subscription, full_premium
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from Home.models import Navigation_link
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest, HttpResponse

# Initialize Razorpay client with API credentials
razorpay_client = razorpay.Client(auth=(settings.RAZORPAY_API_KEY, settings.RAZORPAY_API_SECRET))

@login_required
def create_order(request):
    return render(request, 'payments.html')

@login_required
def create_order1(request):
    if not payment.objects.filter(user=request.user).exists():
        try:
            amount_inrupee = int(subscription.objects.first().cost_of_id_and_volunteer)
            amount = 100 * amount_inrupee  # Amount in paise (50000 paise = 500 INR)
            currency = 'INR'
            receipt = f'order_rcptid_{request.user.id}_{payment.objects.count() + 1}'  # Unique receipt ID

            # Create Razorpay order
            order = razorpay_client.order.create(dict(amount=amount, currency=currency, receipt=receipt))
            order_id = order['id']
            nav_link = Navigation_link.objects.all()

            context = {
                'order_id': order_id,
                'amount': amount,  # Pass this in paise
                'amount_rs' : amount_inrupee,
                'razorpay_merchant_key': settings.RAZORPAY_API_KEY,
                'currency': currency,
                'callback_url': 'success/payment_callback',
                'Navigation_link': nav_link,
            }
            return render(request, 'payment_gateway.html', context)
        except Exception as e:
            messages.error(request, f"Error creating payment order: {e}")
            return redirect('/')
    else:
        messages.info(request, "You have already made a payment.")
        return redirect('/')



@login_required
def create_order2(request):
    
    if payment.objects.filter(user = request.user).exists() == False:
        try:
            amount_inrupee = int(full_premium.objects.first().cost_of_id_and_volunteer)
            amount = 100 * amount_inrupee  # Amount in paise (50000 paise = 500 INR)
            currency = 'INR'
            receipt = f'order_rcptid_{request.user.id}_{payment.objects.count() + 1}'  # Unique receipt ID

            # Create Razorpay order
            order = razorpay_client.order.create(dict(amount=amount, currency=currency, receipt=receipt))
            order_id = order['id']
            nav_link = Navigation_link.objects.all()

            context = {
                'order_id': order_id,
                'amount': amount,  # Pass this in paise
                'amount_rs' : amount_inrupee,
                'razorpay_merchant_key': settings.RAZORPAY_API_KEY,
                'currency': currency,
                'callback_url': 'success/payment_callback2',
                'Navigation_link': nav_link,
            }
            return render(request, 'payment_gateway2.html', context)
        except Exception as e:
            messages.error(request, f"Error creating payment order: {e}")
            return redirect('/')
    elif (int(payment.objects.filter(user = request.user).first().amount) > int(full_premium.objects.first().cost_of_id_and_volunteer)) == False:
        try:
            amount_inrupee = int(full_premium.objects.first().cost_of_id_and_volunteer)
            amount = 100 * amount_inrupee  # Amount in paise (50000 paise = 500 INR)
            currency = 'INR'
            receipt = f'order_rcptid_{request.user.id}_{payment.objects.count() + 1}'  # Unique receipt ID

            # Create Razorpay order
            order = razorpay_client.order.create(dict(amount=amount, currency=currency, receipt=receipt))
            order_id = order['id']
            nav_link = Navigation_link.objects.all()

            context = {
                'order_id': order_id,
                'amount': amount,  # Pass this in paise
                'amount_rs' : amount_inrupee,
                'razorpay_merchant_key': settings.RAZORPAY_API_KEY,
                'currency': currency,
                'callback_url': 'success/payment_callback2',
                'Navigation_link': nav_link,
            }
            return render(request, 'payment_gateway2.html', context)
        except Exception as e:
            messages.error(request, f"Error creating payment order: {e}")
            return redirect('/')
    else:
        messages.info(request, "You have already made a payment.")
        return redirect('/')

@csrf_exempt
def payment_callback(request):
    if request.method == "POST":
        params_dict = {
            'razorpay_order_id': request.POST.get('razorpay_order_id'),
            'razorpay_payment_id': request.POST.get('razorpay_payment_id'),
            'razorpay_signature': request.POST.get('razorpay_signature')
        }

        try:
            # Verify the payment signature
            razorpay_client.utility.verify_payment_signature(params_dict)

            amount_inrupee = int(subscription.objects.first().cost_of_id_and_volunteer)
            payment_save = payment(
                user=request.user,
                amount=amount_inrupee,
                reason='Idcard and volunteer'
            )
            payment_save.save()

            messages.success(request, 'Payment successful! Now you can apply to volunteer.')
            return redirect('/')
        except razorpay.errors.SignatureVerificationError as e:
            messages.error(request, f"Payment verification failed: {e}")
            return HttpResponseBadRequest("Invalid Payment Details")
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")
            return HttpResponseBadRequest("Invalid Request")

    return HttpResponseBadRequest("Invalid Request")

@csrf_exempt
def payment_callback2(request):
    if request.method == "POST":
        params_dict = {
            'razorpay_order_id': request.POST.get('razorpay_order_id'),
            'razorpay_payment_id': request.POST.get('razorpay_payment_id'),
            'razorpay_signature': request.POST.get('razorpay_signature')
        }

        try:
            # Verify the payment signature
            razorpay_client.utility.verify_payment_signature(params_dict)

            amount_inrupee = int(full_premium.objects.first().cost_of_id_and_volunteer)
            payment_save = payment(
                user=request.user,
                amount=amount_inrupee,
                reason='Idcard and volunteer'
            )
            payment_save.save()

            messages.success(request, 'Payment successful! Now you can generate your ID card and apply to volunteer.')
            return redirect('/')
        except razorpay.errors.SignatureVerificationError as e:
            messages.error(request, f"Payment verification failed: {e}")
            return HttpResponseBadRequest("Invalid Payment Details")
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")
            return HttpResponseBadRequest("Invalid Request")

    return HttpResponseBadRequest("Invalid Request")
