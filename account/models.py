# encoding: utf-8
from django.db import models

#用户表
class LoginUser(models.Model):
    email = models.CharField(max_length=255, blank=True)
    passwd = models.CharField(max_length=255, blank=True)
    name = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=255, blank=True)

    class Meta:
        db_table = 'login_user'

