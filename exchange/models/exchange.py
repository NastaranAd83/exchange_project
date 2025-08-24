from django.db import models


class ExchangeAddress(models.Model):
    address_id = models.AutoField(primary_key=True)

    address_desp = models.CharField(max_length=200)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=100)

    
class Exchange(models.Model):
    exchange_zip_code = models.CharField(max_length=100, primary_key=True)
    exchange_name = models.CharField(max_length=100)
    exchange_website = models.URLField(max_length=100)
    exchange_logo = models.ImageField(upload_to='exchange_logos/')
    address_id = models.OneToOneField(ExchangeAddress, on_delete=models.CASCADE,primary_key=True)
    
    staff = models.ManyToManyField('Staff', through='ExchangeStaff', related_name='exchanges')
    currency = models.ManyToManyField('Currency', through='ExchangeCurrency', related_name='exchanges')



class ExchangePhone(models.Model):
    pk = models.CompositePrimaryKey("exchange_zip_code", "phone_number")
    exchange_zip_code = models.ForeignKey(Exchange, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=100)
    phone_type = models.CharField(max_length=50)  
    
    

         


