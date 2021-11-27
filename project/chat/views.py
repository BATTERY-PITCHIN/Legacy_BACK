from django.shortcuts import render

# Create your views here.
def search(request):
    return render(request, 'search.html', {})

# for chatting room
def room(request, room_name):
    return render(request, 'room.html', {
        'room_name': room_name
    })