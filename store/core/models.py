from django.db import models


class BaseImageModel(models.Model):
    image = models.ImageField(
        'изображение',
        upload_to='images',
        blank=True,
        null=True,
    )

    def __str__(self) -> str:
        return self.product.name

    class Meta:
        abstract = True
