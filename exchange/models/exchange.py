


from django.db import models
from .staff import Staff
from .currency import CurrencyType  
from .base_model import BaseModel


class ExchangeAddress(BaseModel):
    address_id = models.AutoField(primary_key=True)
    address_desp = models.CharField(max_length=200)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.street}, {self.city}, {self.country}"


class Exchange(BaseModel):
    exchange_zip_code = models.CharField(max_length=100, primary_key=True)
    exchange_name = models.CharField(max_length=100)
    exchange_website = models.URLField(max_length=100)
    exchange_logo = models.CharField(max_length = 100)
    address = models.OneToOneField(ExchangeAddress, on_delete=models.CASCADE)  # حذف primary_key=True
    
    staff = models.ManyToManyField(Staff, through='ExchangeStaff', related_name='exchanges')
    currency = models.ManyToManyField(CurrencyType, through='ExchangeCurrency', related_name='exchanges')  # استفاده از CurrencyType

    def __str__(self):
        return self.exchange_name


class ExchangePhone(BaseModel):
    exchange = models.ForeignKey(Exchange, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=100)
    phone_type = models.CharField(max_length=50)

    class Meta:
        unique_together = ['exchange', 'phone_number']  # جایگزین CompositePrimaryKey

    def __str__(self):
        return f"{self.exchange.exchange_zip_code} - {self.phone_number}"


class ExchangeStaff(BaseModel):
    exchange = models.ForeignKey(Exchange, on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['exchange', 'staff']

   

class ExchangeCurrency(BaseModel):
    exchange = models.ForeignKey(Exchange, on_delete=models.CASCADE)
    currency = models.ForeignKey(CurrencyType, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['exchange', 'currency']

    


  