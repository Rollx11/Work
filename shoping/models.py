from django.db import models
from django.utils.translation import ugettext_lazy

class Drink(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название напитка")
    drink_title = models.CharField(max_length=100, verbose_name="Тип напитка")
    description = models.CharField(max_length=100, verbose_name="Описание")

    #Возвращение дефолтное значение при оброщении к обьекту
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = ugettext_lazy("напиток")
        verbose_name_plural = ugettext_lazy("напитки")


class Category(models.Model):
    # CharField, IntegerField FloatField и другие- это поля модели
    title = models.CharField(max_length=100, verbose_name='Название Категории', help_text='введите название Категория')
    description = models.CharField(max_length=500, verbose_name='Описание')

    def get_categories(self):
        self.short_description = "Категории"
        return [cat.title for cat in self.categories.all()]

    # возвращение дефолтного значения при обращении к обьекту
    def __str__(self):
        return self.title
    # Изменение заголовка модели в админке

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

