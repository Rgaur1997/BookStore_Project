from rest_framework import serializers
from . import models


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('customer', 'name', 'phone', 'email', 'date_created',)
        model = models.User

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('category','customer','title','Author','Price','Edition',)
        model = models.Book


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('customer','books','date_created',)
        model = models.Order
