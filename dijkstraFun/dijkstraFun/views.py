from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'dijkstraFun/index.html', {'rows':[i for i in range(30)],'columns':[i for i in range(40)]})