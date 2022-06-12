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
    re_path(r'^projectManager.*', TemplateView.as_view(template_name='index.html')),
    re_path(r'^businessManager.*', TemplateView.as_view(template_name='index.html')),
    re_path(r'^Login.*', TemplateView.as_view(template_name='index.html')),
    re_path(r'^home.*', TemplateView.as_view(template_name='index.html')),
    # path('admin/', admin.site.urls),
    path('get_applicant_info/', views.get_applicant_info),
    path('get_pdu_list/', views.get_pdu_list),
    path('get_recruitment_info/', views.get_recruitment_info),
    path('get_project_status_info/', views.get_project_status_info),
    path('get_applicant_region/', views.get_applicant_region),
    path('get_applicant_pic/', views.get_applicant_pic),
    path('get_project_info/', views.get_project_info),
    path('update_applicant_info/', views.update_applicant_info),
    path('delete_project_status_info/', views.delete_project_status_info),
    path('create_project_status/', views.create_project_status),
    path('update_project_status/', views.update_project_status),
    path('update_recruitment_info/', views.update_recruitment_info),
    path('update_project_info/', views.update_project_info),
    path('create_applicant_info/', views.create_applicant_info),
    path('create_recruitment_info/', views.create_recruitment_info),
    path('get_department_list/', views.get_department_list),
    path('get_file_list/', views.get_file_list),
    path('new_download_excel/', views.new_download_excel),
    path('project_status_monthly/', views.project_status_monthly),
    path('save_excel/', views.save_excel),
    path('applicant_according_to_recruitment/', views.applicant_according_to_recruitment),
    path('get_columns/', views.get_columns),
    path('get_common_data/', views.get_common_data),
    path('create_common_info/', views.create_common_info),
    path('get_contact_info/', views.get_contact_info),
    path('update_common_info/', views.update_common_info),
    path('get_status_pic_value/', views.get_status_pic_value),
    path('get_recruitmentInfo_pic/', views.get_recruitmentInfo_pic),
    path('login/', views.login),

]
