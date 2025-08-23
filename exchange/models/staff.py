from django.db import models

class Staff(models.Model):
    national_code = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)
    family = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    


class StaffPhone(models.Model):
    national_code = models.ForeignKey(Staff, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=100)
    phone_type = models.CharField(max_length=50)  
    
    class Meta:
        unique_together = ['national_code', 'phone_number']
       
    






