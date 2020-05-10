from django.urls import path

from . import views

urlpatterns = [
    path("", views.first),
    # path("", views)
    path("register", views.register),
    path("login", views.login),
    path("logout", views.logout),
    path("add_user_info", views.add_user_info),
    path("add_user_info_submit", views.add_user_info_submit),
    path("shops", views.index),
    path("shops/<int:shop_id>", views.shop)
]

