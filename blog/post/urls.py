from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('author', views.author, name='author'),
    path('category1', views.category1, name='category1'),
    path('category2', views.category2, name='category2'),
    path('category3', views.category3, name='category3'),
    path('contacts/', views.contacts, name='contacts'),
    path('single', views.single, name='single'),
    path('register/', views.register, name='register')
]