from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse


# валидация кастомная
# def my_valid_on_7(value):
#     if "7" in value:
#         raise ValidationError('дб 7')
#     raise value
#

class ItemModelManager(models.Manager):
    def is_published(self):
        return super().get_queryset().filter(is_piblished=True)

class CommonInfo(models.Model):
    slug = models.SlugField(max_length=50, db_index=True, unique=True, verbose_name='slug')

    class Meta:
        abstract = True

class Item(CommonInfo):
    name = models.CharField(max_length=255, verbose_name='Название')
    text = models.TextField(blank=True)
    price = models.PositiveIntegerField(help_text='Цена товара')
    photo = models.ImageField(upload_to='photo', null=True)
    is_piblished = models.BooleanField(default=True)
    time_creation = models.DateField(auto_now_add=True)
    cat = models.ForeignKey('Category', on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, verbose_name='пользователь', on_delete=models.CASCADE)

    # можно брать запрос не с миксина, а с менеджера
    # objects_pub = ItemModelManager()

    class Meta:
        ordering = ['cat']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('myapp:item_detail', kwargs={'slug': self.slug})


class Category(CommonInfo):
    title = models.CharField(max_length=255, verbose_name='категория')

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('myapp:category_detail', kwargs={'pk': self.pk})
