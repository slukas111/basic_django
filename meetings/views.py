from django.shortcuts import render, get_object_or_404, redirect
from .models import Meeting, Room
from django.forms import modelform_factory

# function call get. model manager to retrieve from database. 1 private key
def detail(request,id):
    # meetings = Meeting.objects.get(pk=id) return a list of all objects in Meeting table
    # num_meetings = Meeting.objects.count() count of rows in a table
    # Meeting = Meeting.objects.get(pk=5) get that specific object by id from db
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request, "meeting/detail.html", 
    {'meeting': meeting})

def rooms_list(request):
    return render(request, 'meeting/rooms_list.html', {'rooms': Room.objects.all()})

# MeetingForm = modelform_factory(Meeting, fields=['title','data', 'start_time',])
MeetingForm = modelform_factory(Meeting, exclude=[])

# this is a class 
def new(request):
    if request.method == "POST":
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = MeetingForm()
    return render(request, "meeting/new.html", {"form": form})