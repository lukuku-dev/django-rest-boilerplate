from django.contrib import admin
from .models import NoticeArticle, FreeArticle, FreeArticleComment, AskArticle
from common.admin import ModelAdmin

@admin.register(NoticeArticle, FreeArticle, FreeArticleComment, AskArticle)
class BoardsDefaultArticle(ModelAdmin):
    pass