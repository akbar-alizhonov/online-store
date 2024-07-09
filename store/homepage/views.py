from django.views import generic

from catalog.models import Category


class HomePage(generic.ListView):
    queryset = Category.objects.all()
    template_name = 'homepage/category_list.html'
    context_object_name = 'categories'
