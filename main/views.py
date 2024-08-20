from django.shortcuts import render, redirect
from .models import Events
from .forms import EventsForm

# Create your views here.


# @login_required
def events(request):
    events = Events.objects.all()
    return render(request, 'main/events.html', {'events': events})

def create_event(request):
    error = ''
    if request.method == "POST":
        form = EventsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = "Ошибка при заполнении формы"    


    form = EventsForm
    data = {
        'form': form,
        'error': error
    }

    return render(request, 'main/create_event.html', data)

