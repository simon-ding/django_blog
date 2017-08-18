from django.contrib import admin
from .models import Post, Category, Tag
from .forms import ArticleAdminModelForm


class ArticleAdmin(admin.ModelAdmin):
    form = ArticleAdminModelForm

admin.site.register(Post, ArticleAdmin)
admin.site.register(Category)
admin.site.register(Tag)
