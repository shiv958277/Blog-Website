"""social URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include

from django.views.static import serve

from blog.views import index,login,register,profile,newpost,logout,mypost,viewpost,change,update,postpreference,searchbar,updateprofile,popular

urlpatterns = [
    path('',index,name='home'),
    path('login/',login,name='login'),
    path('register/',register,name='register'),
    path('profile/',profile,name='profile'),
    path('newpost/',newpost,name='newpost'),
    path('logout/',logout,name='logout'),
    path('mypost/',mypost,name='mypost'),
    path('viewpost/<int:pk>',viewpost,name='viewpost'),
    path('change/',change,name='change'),
    path('viewpost/edit/<int:pk>',update,name='update'),
    path('postpreference/<int:pk>',postpreference,name='postpreference'),
    path('searchbar/',searchbar,name='searchbar'),
    path('updateprofile/',updateprofile,name='updateprofile'),
    path('popular/',popular,name='popular'),
    path('admin/', admin.site.urls),
    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
    

]
urlpatterns=urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)