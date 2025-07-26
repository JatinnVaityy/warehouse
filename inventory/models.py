from django.db import models

class Product(models.Model): 
    name = models.CharField(max_length=100)
    sku = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)
    def __str__(self):
        return self.name

class StockTransaction(models.Model): 
    TRANSACTION_TYPES = (('IN', 'Stock In'), ('OUT', 'Stock Out'))
    date = models.DateTimeField(auto_now_add=True)
    transaction_type = models.CharField(max_length=3, choices=TRANSACTION_TYPES)
    remarks = models.CharField(max_length=255, blank=True)

class StockDetail(models.Model): 
    transaction = models.ForeignKey(StockTransaction, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()