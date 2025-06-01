from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('book/<int:id>/', views.detail, name='bookdetail'),
    path('authorlist/', views.authorlist, name='authorlist'),
    path('booklist/', views.booklist, name='booklist'),
    path('author/<int:id>/', views.author, name='authordetail'),
]