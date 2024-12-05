from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_order, name='create_order'),
    path('order1', views.create_order1, name='create_order1'),
    path('order2', views.create_order2, name='create_order2'),
    path('success/payment_callback', views.payment_callback, name='payment_callback'),
    path('success/payment_callback2', views.payment_callback2, name='payment_callback'),
]
