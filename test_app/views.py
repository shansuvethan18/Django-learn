from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Room
from .forms import RoomForm
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

def createRoom(request):
    form = RoomForm()
    if request.method =='POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
         

    context={'form':form}
    return render(request, 'test_app/room_form.html', context)


def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.method == 'POST' :
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')

    context ={'form':form}
    return render(request, 'test_app/room_form.html', context)


def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    
    return render(request, 'test_app/delete.html', {'obj':room})

def samplePage(request):
    return render(request, 'test_app/test.html')