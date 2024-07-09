from django.db import models
from catalog import models as catalog_models


class ProductManager(models.Manager):
    def published(self):
        products = (
            self.get_queryset()
            .filter(
                is_published=catalog_models.Product.Published.PUBLISHED
            )
            .select_related('main_image', 'category')
        )
        return products
