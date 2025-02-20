from django.db import models


# Create your models here.

class Users(models.Model):

    username = models.CharField('用户名', max_length=30, unique=True)

    password = models.CharField('密码', max_length=32)

    date_added = models.DateTimeField('创建时间', auto_now_add=True)

    update_date = models.DateTimeField('更新时间', auto_now=True)

    def __str__(self):
        return f"用户：{self.username} + {self.password}"