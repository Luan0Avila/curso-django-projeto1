from django.contrib import admin
from .models import Category, Recipe

# Register your models here.
class Category_admin(admin.ModelAdmin):
    ...


class Recipe_Admin( admin.ModelAdmin):
    ...

@admin.register(Recipe)
class Recipe_Admin( admin.ModelAdmin):
    ...


admin.site.register(Category, Category_admin)