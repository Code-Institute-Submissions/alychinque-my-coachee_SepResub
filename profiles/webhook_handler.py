from django.http import HttpResponse
from .models import Coach

import time

class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        intent = event.data.object
        pid = intent.id
        user = intent.metadata.user
        date_of_birth = intent.metadata.date_of_birth
        gender = intent.metadata.gender
        plan = intent.metadata.plan
        price = intent.metadata.price
        
        billing_details = intent.charges.data[0].billing_details

        coach_exists = False
        attempt = 1
        while attempt <= 5:   
            try:
                coach = Coach.objects.get(
                    name__iexact=billing_details.name,
                    date_of_birth__iexact=date_of_birth,
                    phone_number__iexact=billing_details.phone,
                    gender__iexact=gender,
                    plan__iexact=plan,
                    price__iexact=price,
                    stripe_pid=str(pid),
                )
                coach_exists = True
                break
                
            except Coach.DoesNotExist:
                attempt +=1
                time.sleep(1)
        if coach_exists:
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified Coach already in database',
                status=200)
        else:
            coach = None
            try:
                coach = Coach.objects.create(
                    user= user,
                    name= billing_details.name,
                    date_of_birth= date_of_birth,
                    phone_number= billing_details.phone_number,
                    gender= gender,
                    plan= plan,
                    price= price,
                    stripe_pid= str(pid),
                )
            except Exception as e:
                if coach:
                    coach.delete()
                return HttpResponse(content=f'Webhook received: {event["type"]} | ERROR: {e}',
                status=500)

        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Created coach in webhook',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)