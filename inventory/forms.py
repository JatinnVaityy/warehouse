from django import forms
from .models import Product, StockTransaction, StockDetail

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'sku', 'description']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full border border-gray-400 rounded-md px-3 py-1.5 text-sm',
            }),
            'sku': forms.TextInput(attrs={
                'class': 'w-full border border-gray-400 rounded-md px-3 py-1.5 text-sm',
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full border border-gray-400 rounded-md px-3 py-1.5 text-sm resize-none',
                'rows': 3,
            }),
        }

class StockTransactionForm(forms.ModelForm):
    class Meta:
        model = StockTransaction
        fields = ['transaction_type', 'remarks']
        widgets = {
            'transaction_type': forms.Select(attrs={
                'class': 'w-full border border-gray-400 rounded-md px-3 py-1.5 text-sm bg-white',
            }),
            'remarks': forms.Textarea(attrs={
                'class': 'w-full border border-gray-400 rounded-md px-3 py-1.5 text-sm resize-none',
                'rows': 2,
            }),
        }

class StockDetailForm(forms.ModelForm):
    class Meta:
        model = StockDetail
        fields = ['product', 'quantity']
        widgets = {
            'product': forms.Select(attrs={
                'class': 'w-full border border-gray-400 rounded-md px-3 py-1.5 text-sm bg-white',
            }),
            'quantity': forms.NumberInput(attrs={
                'class': 'w-full border border-gray-400 rounded-md px-3 py-1.5 text-sm',
                'min': 0
            }),
        }
