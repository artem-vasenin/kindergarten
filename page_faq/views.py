from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.views import View

class DetailsView(View):
    """ Контроллер страницы вопросов """
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'page_faq/index.html')