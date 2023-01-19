from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Category)




admin.site.register(models.Post)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'content', 'slug', 'published', 'status')
    search_fields = {'slug': ['title', 'content']}


