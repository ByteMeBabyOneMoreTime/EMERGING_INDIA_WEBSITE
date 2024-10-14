from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('members', views.team_members, name='team'),
    path('id_generation', views.id_card_page, name='id_card'),
    path("joining", views.joining_page, name="joining"),
    path('volunteer-people', views.volunters, name="volunteer panel")
]