
from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
   
    created_at = models.DateTimeField(default=timezone.now, verbose_name="تاریخ ایجاد")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="تاریخ بروزرسانی")
    description = models.TextField(blank=True, null=True, verbose_name="توضیحات")
    
    class Meta:
        abstract = True 
    
    def soft_delete(self):
        
        self.is_active = False
        self.save()
    
    def restore(self):
        
        self.is_active = True
        self.save()

    class Meta:
        abstract = True
        ordering = ['-created_at'] 