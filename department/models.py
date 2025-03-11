from django.db import models

# Create your models here.
class Department(models.Model):
    title = models.CharField(verbose_name='标题', max_length=100)
    count = models.IntegerField(verbose_name='人数')

class Employee(models.Model):

    name = models.CharField(verbose_name='姓名', max_length=100)
    # department = models.ForeignKey(verbose_name='部门', to='Department', to_field='id', on_delete=models.SET_NULL, null=True)  # SET_NULL: 删除该员工时，将department字段设置为null
    # department = models.ForeignKey(verbose_name='部门', to='Department', to_field='id', on_delete=models.SET_DEFAULT, default=1) # SET_DEFAULT: 删除该员工,department字段设置为默认值1
    department = models.ForeignKey(verbose_name='部门', to='Department', to_field='id', on_delete=models.CASCADE) # CASCADE: 删除该部门时，删除该部门下所有员工
    salary = models.IntegerField(verbose_name='薪资')