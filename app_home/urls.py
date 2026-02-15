from django.urls import path

from app_home.views import HomeView


app_name = 'home'

urlpatterns = [
    path('', HomeView.as_view(), name='details'),
]