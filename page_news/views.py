from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.views import View

class DetailsView(View):
    """ Контроллер страницы новости """
    def get(self, request: HttpRequest, slug: str) -> HttpResponse:
        return render(request, 'page_news/index.html')

class ListView(View):
    """ Контроллер страницы новостей """
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'page_news/list.html')