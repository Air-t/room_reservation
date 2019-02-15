from django.contrib import admin
from django.urls import path
from .views import show_rooms, add_room, edit_room, room_details, make_reservation, search_room

urlpatterns = [

    path('address/', show_rooms, name='roomreservation-show_rooms'),
    path('room/new/', add_room, name='roomreservation-add_room'),
    path('room/modify/<int:id>', edit_room, name='roomreservation-edit_room'),
    path('room/<int:id>', room_details, name='roomreservation-room_details'),
    path('reservation/<int:id>/<date>', make_reservation, name=''),
    path('search/', search_room, name='roomreservation-search'),

]