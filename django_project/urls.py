"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url  # include is also here
from django.contrib.auth.models import User
from rest_framework import routers
from rss_24sata import views


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'articles', views.ArticleViewSet)
router.register(r'categories', views.CategoryViewSet)

categ_articles = views.CategoryViewSet.as_view({
    'get': 'articles'
})


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('categories/<int:pk>/articles/', categ_articles)
]
