from django.urls import path

from users.views import socialAuthRequestView, socialLoginView

urlpatterns = [
    path('social/auth', socialAuthRequestView.as_view()),
    path('social/login', socialLoginView.as_view()),
]