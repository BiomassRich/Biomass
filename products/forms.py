from django import forms
from . import models

class addProductsForm(forms.ModelForm):
    class Meta:
        model = models.productsMod
        fields = ['product_type','product_size','source_supplier']
