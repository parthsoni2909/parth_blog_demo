"""blog_writing URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from django.urls import path
from .import views
from django.views.generic import TemplateView
from .views import(
BlogCreateView,
blogdetail,
Blogpage,
BlogUpdateView,
BlogDeleteView,
BlogAPI,
BlogCategoryAPI,
LoginView,
BlogTagAPI
)


urlpatterns = [

    path('',Blogpage,name='home'),
    path('<slug:slug>/',blogdetail,name='blog-detail'),
    path('search/',views.searchblog, name='searchblog'),
    path('newblog/',BlogCreateView.as_view(),name='newblog'),
    path('<slug:slug>/update/',BlogUpdateView.as_view(),name='update'),
    path('<slug:slug>/Delete',BlogDeleteView.as_view(),name='delete'),
    path('v1/BlogList/', BlogAPI.as_view(), name='bloglist'),
    path('v1/BlogCategoryList/', BlogCategoryAPI.as_view(), name='BlogCategoryList'),
    path('v1/BlogTagAPI/', BlogTagAPI.as_view(), name='BlogCategoryList'),
    path('v1/login/', LoginView.as_view(), name='apilogin'),

]
