from django.shortcuts import render
from django.http import JsonResponse

def home(request):
    context = {'name':'Redmi 9 Pro', 'price':20000}
    return render(request, 'home.html', context)

def json_home(request):
    context = {'company':'ABC', 'sector':'ENV'}
    return JsonResponse(context)