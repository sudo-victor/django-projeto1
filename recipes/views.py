from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Victor Souto'
    })


def sobre(request):
    return HttpResponse('HEROU WUROLDE')


def contato(request):
    return render(request, 'temp/temp.html')
