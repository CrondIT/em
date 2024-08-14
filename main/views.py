from django.shortcuts import render

# Create your views here.
def profile_view(request):
    return render(request, 'main/profile.html')

def index(request):
    return render(request,'main/index.html',{})
