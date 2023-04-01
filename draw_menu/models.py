from django.db import models

# Create your models here.
class Point(models.Model):

    menu = models.ForeignKey('self', related_name="points", verbose_name="Меню", null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(verbose_name="Исходный пункт меню", unique=True, max_length=256)
