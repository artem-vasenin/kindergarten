from django.urls import path

from app_pages.views.staff_views import StaffListView


app_name = 'staff'

urlpatterns = [
    path('', StaffListView.as_view(), name='list'),
]