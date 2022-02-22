"""FgBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, re_path
from FgBlog import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView



urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),
    re_path(r'^profile.*', TemplateView.as_view(template_name='index.html')),
    re_path(r'^diary.*', TemplateView.as_view(template_name='index.html')),
    re_path(r'^study.*', TemplateView.as_view(template_name='index.html')),
    re_path(r'^clockIn.*', TemplateView.as_view(template_name='index.html')),
    re_path(r'^qa.*', TemplateView.as_view(template_name='index.html')),
    re_path(r'^difficulty.*', TemplateView.as_view(template_name='index.html')),
    re_path(r'^vpn.*', TemplateView.as_view(template_name='index.html')),
    re_path(r'^hrManageTable.*', TemplateView.as_view(template_name='index.html')),
    re_path(r'^hrManage.*', TemplateView.as_view(template_name='index.html')),
    # path('admin/', admin.site.urls),
    path('getParagraphDetail/', views.getParagraphDetail),
    path('getStudyInfo/', views.studyInfo),
    path('getStudyType/', views.studyType),
    path('getStudyList/', views.studyList),
    path('getStudyTopInfo/', views.getStudyTopInfo),
    path('getStudyMidInfo/', views.getStudyMidInfo),
    path('getStudyBotInfo/', views.getStudyBotInfo),
    path('getStudySwiper/', views.getStudySwiper),
    path('getNavbarList/', views.getNavbarList),
    path('getHtml/', views.getHtml),
    path('get_applicant_info/', views.get_applicant_info),
    path('get_recruitment_info/', views.get_recruitment_info),
    path('get_project_status_info/', views.get_project_status_info),
    path('get_project_info/', views.get_project_info),
    path('update_applicant_info/', views.update_applicant_info),
    path('update_project_status/', views.update_project_status),
    path('update_recruitment_info/', views.update_recruitment_info),
    path('update_project_info/', views.update_project_info),

]
