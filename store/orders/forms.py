from django import forms
from orders import models


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = models.Order
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'city', 'address']
