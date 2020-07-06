"""moobo_project URL Configuration

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
# /usr/bin/python
# -*- coding: utf-8 -*-
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from designer import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('designer/sign_in/', LoginView.as_view(template_name='designer/sign_in.html'), name='designer-sign-in'),
    # path('designer/sign_in/', views.login_in, name='designer-sign-in'),
    path('designer/sign_out/', LogoutView.as_view(next_page='/'), name='designer-sign-out'),
    path('designer/', views.authapp_home, name='authapp-home'),
    path('designer/projects/', views.authapp_home, name='authapp-home'),
    path('designer/sign_up/', views.authapp_sign_up, name='sign-up'),
    path('designer/newproject/', views.new_project, name='new-project'),
    path('designer/projects/newproject/', views.new_project, name='new-project'),
    path('designer/statement/<str:project_name>/', views.statement, name='project-statement'),
    path('designer/statement/<str:project_name>/<int:row>/', views.delete_statement_row, name='delete-statement-row'),
    path('designer/statement/<str:project_name>/pdf/', views.generate_pdf, name='get-statement-pdf'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)