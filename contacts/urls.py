from django.urls import path
from contacts.views import ContactList, ModifyPerson, ViewPerson

urlpatterns = [
    path('', ContactList.as_view(), name='contactlist-contact_list'),
    path('contact/<int:id>/', ViewPerson.as_view(), name='contactlist-contact'),
    path('contact/modify/<int:id>/', ModifyPerson.as_view(), name='contactlist-contact_modify'),
]