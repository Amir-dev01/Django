from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from datetime import datetime
from . import models
from django.views import generic

class SearchBooksView(generic.ListView):
    template_name = 'book.html'
    context_object_name = 'query'

    def get_queryset(self):
        return models.Books.objects.filter(title__icontains=self.request.GET.get('q'))

    def get_context_data(self,*,object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context


#get id
def books_detail(request, id):
    if request.method == 'GET':
        books_id = get_object_or_404(models.Books, id=id)
        return render(
            request,
            template_name='book_detail.html',
            context={
                'books_id': books_id,
            }
        )


#list
def books_list(request):
    if request.method == 'GET':
        query = models.Books.objects.all()
        return render(
            request,
            template_name='book.html',
            context={
                'query': query,
            }
        )



def about_me(request):
    if request.method == "GET":
        return HttpResponse("My name is Amir")

def domestic(request):
    if request.method == "GET":
        html_content = """
               <html>
                   <body>
                       <h1>Bobik</h1>
                       <img src="https://upload.wikimedia.org/wikipedia/ru/b/ba/%D0%90%D0%BA%D1%80%D0%B8%D0%BD%D1%81%D0%BA%D0%B8%D0%B9-%D0%BA%D0%BE%D1%82.jpg" alt="Image" />
                   </body>
               </html>
               """
        return HttpResponse(html_content)


def time(request):
    if request.method == "GET":

        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        html_content = f"""
        <html>
            <body>
                <h1>Текущее время: {current_time}</h1>
            </body>
        </html>
        """
        return HttpResponse(html_content)