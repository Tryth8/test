from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
def mainView(request):

    context = {}
    return render(request, 'main.html', context)
