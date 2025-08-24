from django.db import models
from .exchange import Exchange
from .staff import Staff
from .currency import Currency


class ExchangeStaff(models.Model):
    exchange_zip_code = models.ForeignKey(Exchange, on_delete=models.CASCADE)
    staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['exchange_zip_code', 'staff_id']

    def __str__(self):
        return f"{self.exchange_zip_code} - {self.staff_id}"

class ExchangeCurrency(models.Model):
    exchange_zip_code = models.ForeignKey(Exchange, on_delete=models.CASCADE)
    currency_id = models.ForeignKey(Currency, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['exchange_zip_code', 'currency_id']

    def __str__(self):
        return f"{self.exchange_zip_code} - {self.currency_id}"