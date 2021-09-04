from django.contrib import admin
from django.urls import path
from .views import CreateOrder,ListOrder

urlpatterns = [
   path('create/',CreateOrder.as_view()),
   path('listOrder/',ListOrder.as_view())
]
