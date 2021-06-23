from django.db import models
from django.contrib.auth.models import User


class want(models.Model):

    def __str__(self):
        return self.item_name
        
    item_name = models.CharField(max_length=200)
