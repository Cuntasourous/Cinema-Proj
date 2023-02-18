from django.urls import path
from cine_app import views

#Template tagging
app_name = 'cine_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login'),
]
