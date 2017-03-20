"""manthan2017 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
import os
from settings import BASE_DIR

import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^reg/', views.reg, name='index'),
    url(r'^rate/', views.rate, name='index'),
    url(r'^all/', views.all, name='index'),
    
]+static('/build/', document_root=os.path.join(BASE_DIR,'static/www/build/')) \
              + static('/assets/', document_root=os.path.join(BASE_DIR,'static/www/assets/'))
