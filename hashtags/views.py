from django.shortcuts import render
from . import models
from django.views import generic


class AllCategoryBooksView(generic.ListView):
    model = models.Product
    template_name = 'tags/all_category_books.html'
    context_object_name = 'query'

class TeenCategoryBooksView(generic.ListView):
    model = models.Product
    template_name = 'tags/teen_category_books.html'
    context_object_name = 'query'

    def get_queryset(self):
        return models.Product.objects.filter(tags__name='Книги для подростков')

class KidsCategoryBooksView(generic.ListView):
    model = models.Product
    template_name = 'tags/kids_category_books.html'
    context_object_name = 'query'

    def get_queryset(self):
        return models.Product.objects.filter(tags__name='Книги для детей')