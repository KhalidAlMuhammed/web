from django.contrib import admin
from .models import Article
# Register your models here.

class ArticleAdmin (admin.ModelAdmin):
    list_display = ('title', 'url', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'url': ('title',)}

admin.site.register(Article, ArticleAdmin)