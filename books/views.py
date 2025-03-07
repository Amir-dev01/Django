from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

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