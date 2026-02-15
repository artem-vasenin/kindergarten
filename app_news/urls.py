from django.urls import path

from app_news.views import NewsDetailsView, NewsListView


app_name = 'news'

urlpatterns = [
    path('<slug:slug>/', NewsDetailsView.as_view(), name='details'),
    path('', NewsListView.as_view(), name='list'),
]