from django.db import models


class CustomUser(models.Model):
    username = models.CharField(max_length=50, verbose_name="İstifadəçi adınız")
    name = models.CharField(max_length=50, verbose_name="Adınız")
    surname = models.CharField(max_length=50, verbose_name="Soyadınız")



# Create your models here.
