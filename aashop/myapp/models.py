from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    text = models.TextField(blank=True)
    price = models.PositiveIntegerField(help_text='Цена товара')
    photo = models.ImageField(null=True)
    is_piblished = models.BooleanField(default=True)
    time_creation = models.DateField(auto_now_add=True)