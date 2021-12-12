"""Test_parking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from parking import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', views.login_view, name='login'),
    path('accounts/logout/', views.logout_view, name='logout'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('', views.ParkingList.as_view(), name='index'),
    path('update/<int:pk>/', views.ParkingUpdateView.as_view(), name='update'),
    path('create', views.ParkingCreateView.as_view(), name='create'),
    path('reserve/<int:pk>/', views.ReserveParkingView.as_view(), name='park_reserve')
]
