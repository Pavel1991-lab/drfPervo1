from django.urls import path

from payment.apps import PaymentConfig


from payment.views import CreateCheckoutSessionView

app_name = PaymentConfig.name

urlpatterns = [

   path('create-checkout-session/', CreateCheckoutSessionView.as_view(), name='create-checkout-session'),

]
