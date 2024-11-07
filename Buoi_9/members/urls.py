from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Đường dẫn mặc định cho ứng dụng members
    path('', views.members, name='members'),
]
