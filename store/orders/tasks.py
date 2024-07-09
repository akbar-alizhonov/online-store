from celery import shared_task
from django.core.mail import send_mail
from orders.models import Order


@shared_task
def order_created(order_id: int):
    order = Order.objects.get(id=order_id)
    subject = f'Асалама алейкум брат {order.first_name}'
    message = (
        f'''Братишка твой заказ оформлен.\n\n
        Твой заказ номер: {order_id}\n
        Ждем тебя снова)'''
    )
    send_mail(
        subject=subject,
        message=message,
        from_email='admin@admin.com',
        recipient_list=[order.email]
    )
