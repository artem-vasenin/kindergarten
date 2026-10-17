from django.urls import path

from .views import HomeView


app_name='orders'

urlpatterns = [
    path('', HomeView.as_view(), name='page_home'),
]