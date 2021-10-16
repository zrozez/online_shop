from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'category', 'name', 'amount', 'rating', 'price']
        read_only_fields = ['category', 'rating']

class AmountSerializer(serializers.Serializer):

    amount = serializers.IntegerField()
    

class RatingSerializer(serializers.Serializer):

    rating = serializers.IntegerField()
