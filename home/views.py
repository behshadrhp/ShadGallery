from django.shortcuts import render
from django.views import View


class HomeView(View):
    """
    This class is for render home page.
    """

    def get(self, request):

        context = {}
        return render(request, "main/main.html")
