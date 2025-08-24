from django.db import models

class CurrencyType(models.Model):
    code = models.CharField(max_length=10, unique=True)   
    name = models.CharField(max_length=50, unique=True)   

    def __str__(self):
        return self.code


class CurrencyPrice(models.Model):
    currency = models.ForeignKey(CurrencyType, on_delete=models.CASCADE, related_name="prices")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.currency.code} - {self.price} ({self.date} {self.time})"
