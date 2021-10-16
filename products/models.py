from django.db import models
from django.contrib.auth import get_user_model
from category.models import Category



class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    price = models.IntegerField()
    rating = models.IntegerField()
    amount = models.IntegerField()

    class Meta:
        ordering = ('rating',)

    def __str__(self):
        return self.name    
