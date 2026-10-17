from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.views import View

class DetailsView(View):
    """ Контроллер страницы работника """
    def get(self, request: HttpRequest, slug: str) -> HttpResponse:
        return render(request, 'page_team/index.html')

class ListView(View):
    """ Контроллер страницы работников """
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'page_team/list.html')