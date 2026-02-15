from django.shortcuts import render
from django.views import View


class NewsListView(View):
    def get(self, response):
        return render(response, 'news/list.html')

class NewsDetailsView(View):
    def get(self, response):
        return render(response, 'news/details.html')