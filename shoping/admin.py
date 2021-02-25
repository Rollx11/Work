from django.contrib import admin
from .models import Drink, Category

admin.site.register(Category)

#admin.site.register(Drink)
@admin.register(Drink)
class DrinkAdmin(admin.ModelAdmin):
   # list_display = ["id", "title", "drink_title","description"]
    list_display = ['id', 'title', 'get_categories', 'description']
