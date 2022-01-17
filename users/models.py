from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    USER_REGION_CHOICE = (
        ('BRO', 'Брестская область'),
        ('VIO', 'Витебская область'),
        ('GOO', 'Гомельская область'),
        ('GRO', 'Гродненская область'), 
        ('MIO', 'Минская область'),
        ('MOO', 'Могилевская область'),
        ('MNSK', 'Минск'),
    )
    age = models.PositiveIntegerField(default=0)
    user_region = models.CharField(max_length=20, choices=USER_REGION_CHOICE)
