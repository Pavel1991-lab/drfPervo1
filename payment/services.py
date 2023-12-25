# import os
#
# import stripe
# from rest_framework import status
# from rest_framework.response import Response
#
#
# class StripePayment:
#     stripe.api_key = os.getenv("KEY_STRIPE")
#
#     def __init__(self, paid_object, payment_method, payment_amount):
#         self.paid_object = paid_object
#         self.payment_method = [payment_method]
#         self.payment_amount = payment_amount
#
#     def create(self):
#
#         try:
#             payment_instance = stripe.PaymentIntent.create(
#                 amount=self.payment_amount,
#                 payment_method_types=['card'],
#                 description=f'Payment for {self.paid_object}',
#                 currency='usd'
#             )
#             return payment_instance.id
#         except Exception as e:
#             return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
#
#     @staticmethod
#     def retrieve(stripe_id):
#         return stripe.PaymentIntent.retrieve(stripe_id)