from django.contrib import admin
from .models import Meal, Gallery

class GalleryInline(admin.TabularInline):
    model = Gallery


@admin.register(Meal)
class ProductAdmin(admin.ModelAdmin):
    inlines = [GalleryInline,]
# Register your models here.
