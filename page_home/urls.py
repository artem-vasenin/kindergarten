from django.urls import path

from .views import DetailsView


app_name='page_home'

urlpatterns = [
    path('', DetailsView.as_view(), name='details'),
]