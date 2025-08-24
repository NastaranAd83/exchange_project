from django.db import models
from .exchange import Exchange

class Debt(models.Model):
    debt_id = models.AutoField(primary_key=True)
    debt_amount = models.DecimalField(max_digits=10, decimal_places=2)
    debt_date = models.DateField(auto_now_add=True)
    debt_time = models.TimeField(auto_now_add=True)
    debt_status = models.BooleanField(default=False)
    debt_type = models.CharField(max_length=100)
    debt_description = models.TextField()
    
    debt_exchange = models.ForeignKey(Exchange, on_delete=models.CASCADE)
    