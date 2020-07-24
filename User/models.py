from django.db import models
from django.contrib.auth.models import User
# Create your models here.
CHOICES= [
    ('Register as a User', 'khadok'),
    ('Register as a Rider', 'rider'),
    ('Register as a Store', 'store'),
    ]

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    check = models.CharField(max_length=30)
    def __str__(self):
        return self.user.username