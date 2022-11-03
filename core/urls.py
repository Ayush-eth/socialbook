from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

from django.views.static import serve
from django.urls import re_path as url


urlpatterns = [
    path('',views.index,name="index"),
    path('signup',views.signup,name="signup"),
    path('signin',views.signin,name="signin"),
    path('logout',views.logout,name="logout"),
    path('setting',views.setting,name="setting"),
    path('profile/<str:pk>',views.profile,name="profile"),
    path('follow',views.follow,name="follow"),
    path('upload',views.upload,name="upload"),
    path('search',views.search,name="search"),
    path('like-post',views.like_post,name="like-post"),
    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)