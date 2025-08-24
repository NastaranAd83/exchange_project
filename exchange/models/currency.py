from enum import unique
from django.db import models
from .base_model import BaseModel

class CurrencyType( BaseModel):
    code = models.CharField(max_length=10, unique = True)   
    name = models.CharField(max_length=50, unique=True)   

    def __str__(self):
        return self.code


class CurrencyPrice(BaseModel):
   
    currency_code = models.ForeignKey(CurrencyType, on_delete=models.CASCADE, related_name="prices", to_field="code"  )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)


   