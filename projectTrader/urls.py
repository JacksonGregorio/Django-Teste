from django.contrib import admin
from django.urls import path
from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.user_list, name='user_list'),
    path('user/create/', views.user_create, name='user_create'),
    path('user/<int:pk>/update/', views.user_update, name='user_update'),
    path('user/<int:pk>/delete/', views.user_delete, name='user_delete'),
    path('user/<int:pk>/check', views.check_user, name='check_user'),
    path('user/<int:pk>/zero', views.zero_score, name='zero_score'),
    path('users/order', views.order_by_score, name='order_by_score'),
    path('users/name', views.order_by_name, name='order_by_name'),
    path('users/type', views.order_by_type, name='order_by_type'),
]