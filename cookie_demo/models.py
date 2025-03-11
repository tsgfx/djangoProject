from django.db import models

# Create your models here.
class UserInfo(models.Model):
    """
    用户信息表
    """
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    age = models.IntegerField()
    phone = models.CharField(max_length=100)