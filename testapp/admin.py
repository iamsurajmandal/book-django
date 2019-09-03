from django.contrib import admin
from testapp.models import Book
class Book_admin(admin.ModelAdmin):
    list_display=['title','desc','genre','rating','author']
admin.site.register(Book,Book_admin)

# Register your models here.
