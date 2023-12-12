from django.shortcuts import render
from django.http import JsonResponse

def home(request):
    context = {'name':'Network Adapter', 'price':1500}
    return render(request, 'home.html', context)

def json_home(request):
    context = {'company':'Nyxusbyte', 'sector':'IT'}
    return JsonResponse(context)