from django.db import models

# Create your models here.


class Test01(models.Model):
    """我的测试内容"""
    name = models.CharField(max_length=20)
    sex = models.BooleanField
    age = models.IntegerField(max_length=2)
    birthday = models.DateField
    country = models.CharField(max_length=200)
    province = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    address = models.CharField

    def __str__(self):
        """返回模型的内容"""
        return self.name
