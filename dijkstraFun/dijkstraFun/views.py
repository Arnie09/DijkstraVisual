from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
import json
from dijkstraFun.DijkstraOnGraph import DijkstraGraph

obj = None

# def result(request):
#     if obj is not None:
        

def obstacles(request):
    if request.method == 'POST':
        obstacle_loc = []
        obstacle_loc = request.POST.getlist('arr[]')
        startingPt = request.POST.get('start')
        finalPt = request.POST.get('destination')
        print(startingPt,finalPt)
        startingPt = list(map(int,startingPt.split('-')))
        finalPt = list(map(int,finalPt.split('-')))
        obs_arr = []
        if len(obstacle_loc)>0:
            for elements in obstacle_loc:
                obs_arr.append(list(map(int,elements.split('-'))))
            obj = DijkstraGraph(startingPt,finalPt,obs_arr)
            visited_arr = []
            shortest_path = []
            for elements in obj.visited:
                visited_arr.append(str(elements[0])+'-'+str(elements[1]))
            for elements in obj.shortestPath:
                shortest_path.append(str(elements[0])+'-'+str(elements[1]))
        return JsonResponse({"progress":visited_arr,"path":shortest_path,"accessible":obj.complete})

def index(request):
    return render(request, 'dijkstraFun/index.html', {'rows':[i for i in range(30)],'columns':[i for i in range(40)]})