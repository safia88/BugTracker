"""BugTracker URL Configuration

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
from django.urls import path
from django.conf.urls import include
from BugsApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name='home'),
    path('insert/', views.inserticket,name='insert'),
    path('edit/<int:id>/', views.ticket_edit,name='edit'),
    path('detail/<int:id>/', views.ticket_detail,name='detail'),
    path('invalid/<int:id>/', views.set_invalid,name='invalid'),
    path('assigned/<int:id>/', views.assigned_you, name='assigned'),
    path('completed/<int:id>/', views.completed_you, name='completed'),
    path('logout/', views.logout_action, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
]
