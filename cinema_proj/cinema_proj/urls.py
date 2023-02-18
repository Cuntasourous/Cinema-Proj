"""cinema_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from cine_app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views
from cine_app.views import BookDetailsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cine_app/', include('cine_app.urls')),
    path('', views.index, name='index'),
    path('browse', views.browse, name='browse'),
    path('show_movie/<movie_id>', views.show_movie, name='show_movie'),
    #path('movie/<int:pk>/book', views.CreateBookView.as_view(template_name='cine_app/book_movie.html'), name='book_movie' ),
    path('book_movie/<movie_id>', views.book_movie, name='book_movie'),
    path('book/<int:pk>/', views.BookDetailsView.as_view(template_name='cine_app/show_book.html'), name='show_book'),
    path('booklist/', views.BookListView.as_view(template_name='cine_app/booklist.html'), name='booklist'),
    path('delete//<int:pk>', views.DeleteBookView.as_view(template_name='cine_app/delete.html'), name='delete'),
    path('register/', views.UserRegisterView.as_view(), name='register'),
    #path('register', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login'),
    path('logout', views.user_logout, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

