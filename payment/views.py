import stripe
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView


class CreateCheckoutSessionView(APIView):
    stripe.api_key = 'sk_test_51O5uoRDhwhiDdBd4PS8ygNqNRAXUkoMdty6gN6SqLFazCOAEkUGIDEEm6P6i1tHPGL6MMvr8qE74zAHnTBBvpVdn00ZlaesCDi'
    def post(self, request, *args, **kwargs):
        product_name = request.data.get('product_name')
        unit_amount = request.data.get('unit_amount')

        product = stripe.Product.create(
            name=product_name,
            type='good',  # Тип продукта (например, товар)
            attributes=['size', 'color'],  # Атрибуты продукта
        )
        price = stripe.Price.create(
            unit_amount=unit_amount,  # цена в минимальных единицах валюты (например, центы для USD или евроценты для EUR)
            currency='usd',  # валюта
            product=product.id,  # идентификатор продукта (product) в Stripe
        )
        session = stripe.checkout.Session.create(
            success_url="https://example.com/success",
            cancel_url="https://example.com/cancel",
            payment_method_types=["card"],
            line_items=[
                {
                    "price": price.id,
                    "quantity": 1,
                }
            ],
            mode="payment",
        )

        response_data = {'status': 'success', 'message': 'Payment processed successfully',
                         'payment_url': session.url}
        return Response(response_data, status=status.HTTP_200_OK)