from rest_framework import generics
from .serializers import  NoticeArticleSerializer
from rest_framework.permissions import AllowAny



class NoticeArticleListCreateView(generics.ListCreateAPIView):
    """
        its shows up on the api docs
    """
    serializer_class = NoticeArticleSerializer
    permission_classes = [AllowAny]