from django.db import models
from common.models import IsActiveModel, TimeStampedModel


class NoticeArticle(IsActiveModel, TimeStampedModel):
    writer = models.TextField()
    title = models.TextField()
    content = models.TextField()
    view_count = models.PositiveIntegerField(default=0)


class FreeArticle(IsActiveModel, TimeStampedModel):
    writer = models.TextField()
    title = models.TextField()
    content = models.TextField()
    password = models.TextField()
    view_count = models.PositiveIntegerField(default=0)


class FreeArticleComment(IsActiveModel, TimeStampedModel):
    free_article = models.ForeignKey("FreeArticle", on_delete=models.CASCADE)
    free_article_comment = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)
    is_deleted = models.BooleanField(default=False)
    name = models.TextField()
    content = models.TextField()


class AskArticle(TimeStampedModel):
    company_name = models.TextField()
    name = models.TextField()
    email = models.TextField()
    content = models.TextField()