from django.db import models
from django.contrib.auth import get_user_model
from category.models import Category
from django.core.validators import MaxValueValidator, MinValueValidator

User = get_user_model()

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    price = models.IntegerField()
    rating = models.IntegerField()
    amount = models.IntegerField()

    def __str__(self):
        return self.name 

    @property
    def rating(self):
        ratings = self.ratings.all()
        if ratings:
            sum_ = 0
            for rating in ratings:
                sum_ += rating.value
            return round(sum_/len(ratings), 2)
        return 0

class Rating(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='ratings')
    value = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
