from django.contrib import admin
from .models import Book


@admin.register(Book)
class bookadmin(admin.ModelAdmin):
    list_display = ['id', 'title']



# admin.site.register(Book)
