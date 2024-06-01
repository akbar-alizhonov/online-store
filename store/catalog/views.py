from django.db.models.query import QuerySet
from django.views import generic
from django.shortcuts import get_object_or_404

from catalog import models
from cart.forms import CartAddProductForm


class ProductList(generic.ListView):
    template_name = 'catalog/product_list.html'
    queryset = models.Product.objects.published()
    context_object_name = 'products'


class CategoryDetail(generic.ListView):
    template_name = 'catalog/products_by_category.html'
    context_object_name = 'products'

    def get_queryset(self) -> QuerySet[models.Product]:
        category = get_object_or_404(
            models.Category,
            slug=self.kwargs['slug']
        )
        category_products = (
            models.Product.objects
            .filter(
                category=category,
                is_published=models.Product.Published.PUBLISHED,
            )
            .select_related('category')
        )

        return category_products


class ProductDetail(generic.DetailView):
    model = models.Product
    template_name = 'catalog/product_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart_add_form'] = CartAddProductForm()
        return context
