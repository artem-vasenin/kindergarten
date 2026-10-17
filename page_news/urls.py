from django.urls import path

from .views import ListView, DetailsView


app_name='news'

urlpatterns = [
    path('', ListView.as_view(), name='list'),
    path('<slug:slug>/', DetailsView.as_view(), name='details'),
]