from django.shortcuts import render
from .models import Volunteer_form
from Home.models import *
def volunteer_list(request):
    anounce = announcement.objects.all()
    nav_link = Navigation_link.objects.all()
    volunteers = Volunteer_form.objects.select_related('user').all()
    return render(request, 'volunteers_details.html', {'volunteers': volunteers, "announcement": anounce, "Navigation_link": nav_link})
