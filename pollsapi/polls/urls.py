from django.urls import path, include
from polls import views

# URLS ------------------------------------

urlpatterns = [
    path('polls/',views.poll_lists, name='poll_lists'),
    path('polls/<int:pk>/',views.poll_details, name='poll_details'),
]