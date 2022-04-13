from django.db import models
from django.contrib.auth.models import User

BOOKS_CHOICES =(
    ("1", "Mystery & Thriller"),
    ("2", "History"),
    ("3", "Romance"),
    ("4", "Childeren & Young Adults"),
    ("5", "Literature & Fiction"),
    ("6", "Biographies"),
    ("7", "Business"),
    ("8", "Health"),
    ("9", "art"),
)

# Create your models here.

class User(models.Model):
    customer = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.name)


class Book(models.Model):
    category = models.CharField(choices=BOOKS_CHOICES, max_length=80, blank=True, null=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=True)
    Author = models.CharField(max_length=200, null=True)
    Price = models.IntegerField()
    Edition = models.IntegerField(null=True)

    def __str__(self):
        return str(self.title)


class Order(models.Model):
    customer = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    books = models.ForeignKey(Book, null=True, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.customer)
