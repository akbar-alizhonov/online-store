from django import forms
from catalog import models


class ProductForm(forms.ModelForm):
    class Meta:
        model = models.Product
        fields = ['name', 'slug', 'description', 'category', 'price']
