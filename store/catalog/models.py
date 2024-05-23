from django.db import models
from django.utils.translation import gettext_lazy as _
from core import models as abs_models
from catalog.managers import ProductManager


class Category(models.Model):
    name = models.CharField(
        verbose_name='название',
        max_length=100,
        unique=True,
    )
    slug = models.SlugField(
        'слаг',
        unique=True,
    )

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    objects = ProductManager()

    class Published(models.TextChoices):
        PUBLISHED = 'Да', _('Опубликовано')
        DRAFT = 'Нет', _('Черновик')

    name = models.CharField(
        verbose_name='название',
        max_length=255,
    )
    slug = models.SlugField(
        'слаг',
        unique=True,
    )
    is_published = models.TextField(
        'опубликовано',
        max_length=3,
        choices=Published,
        default=Published.PUBLISHED,
    )
    description = models.TextField('описание товара')
    created = models.DateField('дата создания', auto_now_add=True)
    category = models.ForeignKey(
        Category,
        verbose_name='категория',
        on_delete=models.CASCADE,
    )
    price = models.PositiveIntegerField('цена')

    def __str__(self) -> str:
        return self.name


class MainImage(abs_models.BaseImageModel):
    product = models.OneToOneField(
        Product,
        verbose_name='товар',
        related_name='main_image',
        on_delete=models.CASCADE,
    )


class Image(abs_models.BaseImageModel):
    product = models.ForeignKey(
        Product,
        verbose_name='товар',
        related_name='images',
        on_delete=models.CASCADE,
    )
