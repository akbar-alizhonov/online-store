from django.db.models.query import QuerySet
from django.views import generic
from django.shortcuts import get_object_or_404

from catalog import models


class ProductList(generic.ListView):
    template_name = 'catalog/product_list.html'
    queryset = models.Product.objects.published()
    context_object_name = 'products'


class CategoryDetailProducts(generic.ListView):
    template_name = 'catalog/category_detail.html'
    context_object_name = 'products'

    def get_queryset(self) -> QuerySet[models.Product]:
        category = get_object_or_404(
            models.Category,
            slug=self.kwargs['slug']
        )
        category_products = (
            models.Product.objects
            .filter(category=category)
            .select_related('category')
        )

        return category_products
