from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse


# валидация кастомная
# def my_valid_on_7(value):
#     if "7" in value:
#         raise ValidationError('дб 7')
#     raise value
#

class Item(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    text = models.TextField(blank=True)
    price = models.PositiveIntegerField(help_text='Цена товара')
    photo = models.ImageField(upload_to='photo', null=True)
    is_piblished = models.BooleanField(default=True)
    time_creation = models.DateField(auto_now_add=True)
    slug = models.SlugField(max_length=50, db_index=True, unique=True, verbose_name='slug')
    cat = models.ForeignKey('Category', on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['cat']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('myapp:item_detail', kwargs={'slug': self.slug})


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='категория')
    slug = models.SlugField(max_length=50, db_index=True, unique=True, verbose_name='slug')

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('myapp:category_detail', kwargs={'pk': self.pk})
