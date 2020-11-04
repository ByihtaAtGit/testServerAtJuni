from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

import os




def index(request):
	times = int(os.environ.get('TIMES',3))
	return HttpResponse('Hello' * times)
	
def myView(request):
	return HttpResponse("Hello, World Ahhhhh!")	


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
