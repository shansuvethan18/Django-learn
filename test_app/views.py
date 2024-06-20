from django.shortcuts import render
from django.http import HttpResponse
from .models import Room

# rooms = [
#     {'id':1,'name':'Lets learn Python!'},
#     {'id':2,'name':'Design!'},
#     {'id':3,'name':'Lets learn Java!'}
# ]

# Create your views here.
def home(request):
    rooms = Room.objects.all()
    context = {'rooms':rooms}
    return render(request, 'test_app/home.html', context)

def room(request,pk):
    room= Room.objects.get(id=pk)
    #room = None
    # for i in rooms:
    #     if i['id'] == int(pk):
    #         room = i
    context = {'room':room}

    return render(request, 'test_app/room.html',context)