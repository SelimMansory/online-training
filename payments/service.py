import stripe
import os


def create_payment(title: str, price: float):
    """
    Создание продукта в сервисе stripe
    """

    stripe.api_key = os.getenv('STRIPE_API_KEY')

    starter_subscription = stripe.Product.create(
        name=title,
        description=f"${price}",
    )

    starter_subscription_price = stripe.Price.create(
        unit_amount=price * 100,
        currency="usd",
        product=starter_subscription['id'],
    )

    checkout = stripe.checkout.Session.create(
        success_url="https://example.com/success",
        line_items=[
            {
                "price": starter_subscription_price['id'],
                "quantity": 1,
            },
        ],
        mode="payment",
    )

    return (checkout['url'], checkout['id'])


def payment_verification(payment_id):
    """
    Проверка платежа в сервисе stripe
    """
    stripe.api_key = os.getenv('STRIPE_API_KEY')

    checkout = stripe.checkout.Session.retrieve(
        payment_id,
    )

    return checkout['payment_status']