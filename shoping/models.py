from django.db import models
from django.utils.translation import ugettext_lazy

class Category(models.Model):

    title = models.CharField(max_length=100, verbose_name='Название Категории', help_text='введите название Категория')
    description = models.CharField(max_length=500, verbose_name='Описание')

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"




class Drink(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название напитка")
    drink_title = models.CharField(max_length=100, verbose_name="Тип напитка")
    description = models.CharField(max_length=100, verbose_name="Описание")
    categories = models.ManyToManyField(Category, verbose_name='категория', )



    def __str__(self):
        return self.title

    class Meta:
        verbose_name = ugettext_lazy("напиток")
        verbose_name_plural = ugettext_lazy("напитки")

    def get_categories(self):
        self.short_description = "Категории"
        return [cat.title for cat in self.categories.all()]












