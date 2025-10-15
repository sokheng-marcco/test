from django import forms
from .models import Product, Category

class CategoryForm (forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        
class ProductForm (forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'cost_price', 'selling_price', 'unit']
