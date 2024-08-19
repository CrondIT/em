from django.shortcuts import render
from .models import Events

# Create your views here.


# @login_required
def events(request):
    events = Events.objects.all()
    return render(request, 'main/events.html', {'events': events})

def create_event(request):
    return render(request, 'main/create_event.html')

