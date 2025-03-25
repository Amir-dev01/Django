from django.urls import path
from . import views

urlpatterns = [
    path("about_me/", views.about_me),
    path("domestic/", views.domestic),
    path("time/", views.time),
    path('', views.BooksListView.as_view(),name='books'),
    path('books_list/<int:id>/', views.BooksDetailView.as_view()),
    path('search/',views.SearchBooksView.as_view(),name='search'),
]