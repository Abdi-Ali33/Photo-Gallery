from django.contrib import admin
from .models import Location, Category, Image


# class LocationAdmin(admin.ModelAdmin):
#     prepopulated_fields = {"slug": ("name",)}


# class CategoryAdmin(admin.ModelAdmin):
#     prepopulated_fields = {"slug": ("name",)}


# Register your models here.
admin.site.register(Location)
admin.site.register(Category)
admin.site.register(Image)
