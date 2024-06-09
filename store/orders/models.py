from django.db import models
from catalog.models import Product


class Order(models.Model):
    first_name = models.CharField('имя', max_length=100)
    last_name = models.CharField('фамилия', max_length=100)
    phone_number = models.CharField('номер телефона', max_length=100)
    email = models.EmailField('почта')
    address = models.CharField('адрес', max_length=250)
    city = models.CharField('город', max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'Заказ номер {self.id}'

    def get_total_cost(self):
        return sum(product.get_cost() for product in self.products.all())


class OrderItem(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='order_products'
    )
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='products'
    )
    price = models.PositiveBigIntegerField('цена')
    quantity = models.PositiveSmallIntegerField('количество')

    def __str__(self) -> str:
        return f'Продукт {self.price.id}'

    def get_cost(self):
        return self.price * self.quantity
