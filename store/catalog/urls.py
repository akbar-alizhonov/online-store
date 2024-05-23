from django.urls import path
from catalog import views


app_name = 'catalog'

urlpatterns = [
    path('', views.ProductList.as_view(), name='product_list'),
    path(
        'category/<slug:slug>/products',
        views.CategoryDetailProducts.as_view(),
        name='category_detail'
    )

]
