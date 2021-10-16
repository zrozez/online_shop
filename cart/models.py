from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.dispatch import receiver

from rest_framework.decorators import action

from products.models import Product

User = get_user_model()

class Cart(models.Model):

    owner = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='cart')
    products = models.ManyToManyField(Product, through='CartProduct')


class CartProduct(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cart_products')
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_products')
    amount = models.IntegerField(default=1)
    date_added = models.DateTimeField(auto_now_add=True)

    @receiver(post_save, sender=User)
    def create_cart(sender, instance, created, **kwargs):

        if created:
            CartProduct.objects.create(mentor=instance)
            

    @action(methods=['get', ], detail=True)
    def total_amount(self, request, *args, **kwargs):
        cart = request.user.cart
        cartproducts = cart.cartproduct_set.all()
        product_list = ''
        total_amount = 0
        total_price = 0
        for cartproduct in cartproducts:
            product_list += f'{cartproduct.product.name}, '
            total_price += cartproduct.product.price * cartproduct.amount
            total_amount += cartproduct.amount
