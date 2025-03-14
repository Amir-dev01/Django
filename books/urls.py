from django.urls import path
from . import views

urlpatterns = [
    path("about_me/", views.about_me),
    path("domestic/", views.domestic),
    path("time/", views.time),
    path('', views.books_list),
    path('books_list/<int:id>/', views.books_detail),
]