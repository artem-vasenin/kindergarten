from django.urls import path

from .views import DetailsView


app_name='faq'

urlpatterns = [
    path('', DetailsView.as_view(), name='details'),
]