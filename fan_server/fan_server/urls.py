"""
URL configuration for fan_server project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from bulletin_board import views


urlpatterns = [
    path('register/', views.register_user, name='register_user'),
    path('bulletin/create/', views.create_bulletin, name='create_bulletin'),
    path('bulletin/edit/<int:bulletin_id>/', views.edit_bulletin, name='edit_bulletin'),
    path('bulletin/detail/<int:bulletin_id>/', views.bulletin_detail, name='bulletin_detail'),
    path('user/responses/', views.user_responses, name='user_responses'),
]
