from django import forms
from orders import models


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = models.Order
        fields = ['phone_number', 'city', 'address']
