from django.db import models

# Create your models here.
class UserInfo(models.Model):
    name = models.CharField(verbose_name='Name', max_length=100)
    age = models.IntegerField(verbose_name='Age')
    email = models.EmailField(verbose_name='Email')
    password = models.CharField(verbose_name='Password', max_length=100, default='123456Qq')