from django.urls import path

from .views import DetailsView, ListView


app_name='team'

urlpatterns = [
    path('', ListView.as_view(), name='list'),
    path('<slug:slug>', DetailsView.as_view(), name='details'),
]