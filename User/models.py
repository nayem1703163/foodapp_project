from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    check = models.CharField(max_length=30)
<<<<<<< HEAD
=======


>>>>>>> 51d8b1408e3c24ab8a52f064ffbfbaa08437b939
    def __str__(self):
        return self.check
