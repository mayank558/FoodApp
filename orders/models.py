from django.db import models

from User.models import User


# Create your models here.
class Order(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    owner = models.ForeignKey(to=User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title