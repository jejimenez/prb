"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from authentication.views import LoginView, LogoutView
from .views import IndexPoolingView



urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    #
    url(r'^social/', include('rest_framework_social_oauth2.urls')),
    #url(r'^social/', include('social_auth.urls')),
    #url('', include('social.apps.django_app.urls')),
    #url(r'^social/', include('social.apps.django_app.urls', namespace='social')),
    #url(r'^auth/', include('rest_framework_social_oauth2.urls')),
    url(r'^$',IndexPoolingView.as_view(),name='index'),
    url(r'^', include('authentication.urls')),
    url(r'^', include('pooling.urls')),
    #
    #url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]
