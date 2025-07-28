from django import forms
from .models import Product, StockTransaction, StockDetail

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'sku', 'description']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full border border-gray-400 rounded-md px-3 py-1.5 text-sm',
                'required': True,
                'maxlength': 100,
                'placeholder': 'Product Name',
            }),
            'sku': forms.TextInput(attrs={
                'class': 'w-full border border-gray-400 rounded-md px-3 py-1.5 text-sm',
                'required': True,
                'maxlength': 50,
                'placeholder': 'Stock Keeping Unit (SKU)',
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full border border-gray-400 rounded-md px-3 py-1.5 text-sm resize-none',
                'rows': 3,
                'maxlength': 500,
                'placeholder': 'Description (optional)',
            }),
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name or not name.strip():
            raise forms.ValidationError("Product name is required.")
        return name

    def clean_sku(self):
        sku = self.cleaned_data.get('sku')
        if not sku or not sku.strip():
            raise forms.ValidationError("SKU is required.")
        if Product.objects.filter(sku=sku).exists():
            raise forms.ValidationError("SKU must be unique.")
        return sku

class StockTransactionForm(forms.ModelForm):
    class Meta:
        model = StockTransaction
        fields = ['transaction_type', 'remarks']
        widgets = {
            'transaction_type': forms.Select(attrs={
                'class': 'w-full border border-gray-400 rounded-md px-3 py-1.5 text-sm bg-white',
                'required': True,
            }),
            'remarks': forms.Textarea(attrs={
                'class': 'w-full border border-gray-400 rounded-md px-3 py-1.5 text-sm resize-none',
                'rows': 2,
                'maxlength': 255,
                'placeholder': 'Remarks (optional)',
            }),
        }

class StockDetailForm(forms.ModelForm):
    class Meta:
        model = StockDetail
        fields = ['product', 'quantity']
        widgets = {
            'product': forms.Select(attrs={
                'class': 'w-full border border-gray-400 rounded-md px-3 py-1.5 text-sm bg-white',
                'required': True,
            }),
            'quantity': forms.NumberInput(attrs={
                'class': 'w-full border border-gray-400 rounded-md px-3 py-1.5 text-sm',
                'min': 1,
                'required': True,
                'placeholder': 'Quantity',
            }),
        }

    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        if quantity is None or quantity < 1:
            raise forms.ValidationError("Quantity must be at least 1.")
