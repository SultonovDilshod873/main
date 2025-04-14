from django.db import models
class Elon (models.Model):
    # E'lon uchun turli maydonlar
    title= models.CharField(max_length=100) # E'lon nomi 
    description = models.TextField() # E'lon tavsifi
    price=models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True) # Narxi
    created_at=models.DateTimeField(auto_now_add=True) # E'lon yaratish vaqti
    updated_ad=models.DateTimeField(auto_now=True) # E'lonni oxirgi taxlil qilish vaqti 
    def __str__(self):
        return self.title
    

# Create your models here.
