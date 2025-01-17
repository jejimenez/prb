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
from authentication.views import LoginView, LogoutView, AccountViewSet, social_login
from rest_framework_nested import routers

# add accounts/ url pattern to be added to urlpatterns variable 
#router = routers.SimpleRouter()
#router.register(r'accounts', AccountViewSet)



urlpatterns = [
    #url(r'^api/v1/', include(router.urls)),
    url(r'^api/v1/auth/login/$', LoginView.as_view(), name='login'),
    url(r'^api/v1/auth/sociallogin/$', social_login),#register_by_access_token),
    url(r'^api/v1/auth/logout/$', LogoutView.as_view(), name='logout'),
]
