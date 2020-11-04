from django.shortcuts import render
from django.http import HttpResponse
import os




def index(request):
	times = int(os.environ.get('TIMES',3))
	return HttpResponse('Hello' * times)
	
def myView(request):
	return HttpResponse("Hello, World Ahhhhh!")
	
