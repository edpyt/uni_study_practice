from django.contrib import admin
from django.urls import path

from user_interact import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="user_interact_index"),
]
