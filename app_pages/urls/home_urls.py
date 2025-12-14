from django.urls import path

from app_pages.views.home_views import HomeView


app_name = 'home'

urlpatterns = [
    path('', HomeView.as_view(), name='details'),
]