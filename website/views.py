from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from meetings.models import Meeting

# normal python function, 'view function'
def welcome(request):
    return render(request, "website/welcome.html", {'meetings': Meeting.objects.all()}
    # {'message': "this will render to the page", 'x': 42, 'name': "sasha", 'age': 32}
    )
#dict {'key=variable name// goes to html : value=data}

def date(request):
    return HttpResponse("this page is served at " + str(datetime.now()))

def about(request):
    return HttpResponse("I am sasha and finally learning django")