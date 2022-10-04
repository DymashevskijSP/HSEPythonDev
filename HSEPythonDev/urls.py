"""HSEPythonDev URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import re_path, include
from rest_framework.routers import SimpleRouter

from HSEPythonDev.src.core.views import HelloWorldViewSet, MeetingsViewSet
hello_world_router = SimpleRouter()
hello_world_router.register('hello', HelloWorldViewSet, basename='hello')

meetingsRouter = SimpleRouter()
meetingsRouter.register('meetings', MeetingsViewSet, basename='meetings')
urlpatterns = [
    re_path(r'test/', include(hello_world_router.urls)),
    re_path(r'', include(meetingsRouter.urls))
]
