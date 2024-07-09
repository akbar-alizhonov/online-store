from django.contrib import admin
from catalog import models


class MainImageInline(admin.TabularInline):
    model = models.MainImage


class ImageInline(admin.TabularInline):
    model = models.Image


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Product)
class ProdcutAdmin(admin.ModelAdmin):
    inlines = [MainImageInline, ImageInline]
