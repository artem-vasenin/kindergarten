from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.views import View

class DetailsView(View):
    """ Контроллер главной страницы """
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'page_home/index.html')
