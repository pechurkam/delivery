from django.contrib import admin
from .models import Shop, Location, Dish, Courier, Client, Order, DishOrder

# Register your models here.
admin.site.register(Shop)
admin.site.register(Location)
admin.site.register(Dish)
admin.site.register(Courier)
admin.site.register(Client)
admin.site.register(Order)
admin.site.register(DishOrder)
