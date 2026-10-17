from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.views import View

class DetailsView(View):
    """ Контроллер страницы документов """
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'page_docs/index.html')