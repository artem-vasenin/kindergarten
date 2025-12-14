from django.shortcuts import render
from django.views import View


class StaffListView(View):
    def get(self, response):
        return render(response, 'staff/details.html')
