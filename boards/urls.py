from django.urls import path
from .views import NoticeArticleListCreateView

urlpatterns = [
    path('notice-articles/', NoticeArticleListCreateView.as_view()),
]
