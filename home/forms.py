from django import forms
from .models import orders
class OrderForm(forms.ModelForm):
    class Meta:
        model =orders
        fields=['name','mobile','address']
        labels={'name':'Name','mobile':'Mobile Number','address':'Address'}