from django.contrib import admin
from django.urls import path

from django.http import JsonResponse
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView


def hello_world_view(request):
    data = {'message': 'hello world'}

    return JsonResponse(data)


urlpatterns = [
    path('', hello_world_view),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/docs/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('admin/', admin.site.urls),
]
