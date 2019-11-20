from django.http import HttpResponse
from django.shortcuts import render
import json

def obstacles(request):
    print("hello there")
    if request.method == 'POST':
        obstacle_loc = []
        obstacle_loc = request.POST.getlist('arr[]')
        print(obstacle_loc)
        return HttpResponse('Success')

def index(request):
    return render(request, 'dijkstraFun/index.html', {'rows':[i for i in range(30)],'columns':[i for i in range(40)]})