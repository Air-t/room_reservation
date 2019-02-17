from django.contrib import admin
from django.urls import path
from contacts.views import ContactList

urlpatterns = [
    path('', ContactList.as_view(), name='contactlist-contact_list')
]