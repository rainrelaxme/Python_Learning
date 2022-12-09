from django.db import models

# Create your models here.


class Pizza(models.Model):
    """披萨的模型"""
    name = models.CharField(max_length=200)
    size = models.FloatField(blank=True)    # blank允许为空
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """返回模型的字符串表示"""
        return self.name

    def __float__(self):
        """返回模型的float表示"""
        return self.size


class Topping(models.Model):
    """披萨的配料表"""
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """返回模型的字符串表示"""
        if len(self.name) > 50:
            return self.name[:50] + "..."
        else:
            return self.name
