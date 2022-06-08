from rest_framework import serializers
from .models import NoticeArticle


class NoticeArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = NoticeArticle
        fields = ['writer', 'title', 'content', 'view_count']
