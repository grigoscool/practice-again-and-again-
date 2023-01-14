from django.db import models
from django.urls import reverse


class Item(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    text = models.TextField(blank=True)
    price = models.PositiveIntegerField(help_text='Цена товара')
    photo = models.ImageField(upload_to='photo', null=True)
    is_piblished = models.BooleanField(default=True)
    time_creation = models.DateField(auto_now_add=True)
    slug = models.SlugField(max_length=50, db_index=True, unique=True, verbose_name='slug')
    cat = models.ForeignKey('Category', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('item_detail', kwargs={'pk': self.pk})


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='категория')
    slug = models.SlugField(max_length=50, db_index=True, unique=True, verbose_name='slug')


    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'pk': self.pk})
