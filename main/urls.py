from django.urls import path, include

from . import views
from main.views import profile_view

urlpatterns = [
   path('profile',profile_view, name='profile'),
   path('',views.index, name='index'),
]