from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, StockTransaction, StockDetail
from .forms import ProductForm, StockTransactionForm, StockDetailForm
from django.db.models import Sum
from django.views.decorators.http import require_POST

def product_list(request):
    products = Product.objects.all()
    return render(request, 'inventory/product_list.html', {'products': products})

def product_create(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('product_list')
    return render(request, 'inventory/product_form.html', {'form': form})

def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid():
        form.save()
        return redirect('product_list')
    return render(request, 'inventory/product_form.html', {'form': form})

def transaction_list(request):
    transactions = StockTransaction.objects.all().order_by('-date')
    return render(request, 'inventory/transaction_list.html', {'transactions': transactions})

def transaction_create(request):
    if request.method == 'POST':
        tx_form = StockTransactionForm(request.POST)
        if tx_form.is_valid():
            transaction = tx_form.save()
            # Handle multiple products in transaction
            for key in request.POST:
                if key.startswith('product_'):
                    product_id = key.split('_')[1]
                    quantity = int(request.POST[key])
                    if quantity > 0:
                        StockDetail.objects.create(
                            transaction=transaction,
                            product_id=product_id,
                            quantity=quantity
                        )
            return redirect('transaction_list')
    else:
        tx_form = StockTransactionForm()
        products = Product.objects.all()
    return render(request, 'inventory/transaction_form.html', {'tx_form': tx_form, 'products': products})

def inventory_summary(request):
    products = Product.objects.all()
    summary = []
    for product in products:
        in_qty = StockDetail.objects.filter(product=product, transaction__transaction_type='IN').aggregate(Sum('quantity'))['quantity__sum'] or 0
        out_qty = StockDetail.objects.filter(product=product, transaction__transaction_type='OUT').aggregate(Sum('quantity'))['quantity__sum'] or 0
        current_stock = in_qty - out_qty
        summary.append({'product': product, 'stock': current_stock})
    return render(request, 'inventory/inventory_summary.html', {'summary': summary})

@require_POST
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('inventory_summary')

@require_POST
def transaction_delete(request, pk):
    transaction = get_object_or_404(StockTransaction, pk=pk)
    transaction.delete()
    return redirect('transaction_list')