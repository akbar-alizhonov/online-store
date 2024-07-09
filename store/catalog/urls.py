from django.urls import path
from catalog import views


app_name = 'catalog'

urlpatterns = [
    path('', views.ProductList.as_view(), name='product_list'),
    path(
        'category/<slug:slug>/',
        views.ProductListByCategory.as_view(),
        name='products_by_category'
    ),
    path(
        'product/<int:id>/<slug:slug>/',
        views.ProductDetail.as_view(),
        name='product_detail'
        ),
]
