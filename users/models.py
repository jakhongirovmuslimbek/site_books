from django.db import models
from django.contrib.auth.models import AbstractUser 

class UsersModel(AbstractUser):
   username = None
   telegram_id = models.CharField(max_length=150, unique=True)
   lang = models.CharField(max_length=2, default='uz')
   
   USERNAME_FIELD = 'telegram_id'

   def __str__(self):
      return self.telegram_id

