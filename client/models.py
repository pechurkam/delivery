from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class Shop(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=64)
    category = models.CharField(max_length=64)
    image = models.ImageField(blank=False, default="https://res.cloudinary.com/glovoapp/w_680,h_240,c_fit,f_auto,"
                                                   "q_auto/Products/phfj7p3w7dhjpxzovqk6")

    def __str__(self):
        return f"{self.id} : name {self.name}, desc {self.description}, category {self.category}"


class Location(models.Model):
    address = models.CharField(max_length=64)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name="locations")

    def __str__(self):
        return f"{self.id} : address {self.address}"


class Dish(models.Model):
    name = models.CharField(max_length=64)
    category = models.CharField(max_length=64)
    description = models.CharField(max_length=64)
    weight = models.IntegerField()
    price = models.IntegerField(blank=False, default=0)
    image = models.ImageField(blank=False, default="https://res.cloudinary.com/glovoapp/w_680,h_240,c_fit,f_auto,"
                                                   "q_auto/Products/phfj7p3w7dhjpxzovqk6")
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name="dishes", default=None)

    def __str__(self):
        return f"{self.id} : name {self.name}, category {self.category}, desc {self.description}, " \
               f"weight {self.weight}"


class Courier(models.Model):
    phone = models.CharField(max_length=13)
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.id} : phone {self.phone}, name {self.name}"


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=13)
    address = models.CharField(max_length=64)
    card = models.CharField(max_length=16)

    def __str__(self):
        return f"{self.id} : phone {self.phone}, address {self.address}, " \
               f"card {self.card}"


class Order(models.Model):
    notes = models.CharField(max_length=64)
    paid = models.BooleanField(default=False)
    delivered = models.BooleanField(default=False)
    date = models.DateTimeField(default=datetime.now, blank=True)
    payment = models.BooleanField(default=False)
    courier = models.ForeignKey(Courier, on_delete=models.CASCADE, related_name="orders", default=1)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="orders")

    def __str__(self):
        return f"{self.id} : notes {self.notes}, paid {self.paid}, " \
               f"delivered {self.delivered}, date {self.date}, payment {self.payment}"


class DishOrder(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, related_name="dish_in_DishOrder")
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order_in_DishOrder")
    amount = models.IntegerField()

    def __str__(self):
        return f"{self.id}: amount {self.amount}"






