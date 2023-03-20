from django.db import models

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=150, null=True, blank=True)
    description = models.TextField(max_length = 150, null=True, blank=True)
    price = models.FloatField(default =50.5, null=True, blank=True)
    image = models.ImageField(upload_to = 'products/', null=True, blank=True)

    def __str__(self):
        return self.name


