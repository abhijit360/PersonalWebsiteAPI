from django.contrib import admin
from django.urls import path
from .views import PostContact

urlpatterns = [
    path('createResponse/', PostContact),

]
