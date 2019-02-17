from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from contacts.forms import PersonForm
from contacts.models import Person


class ContactList(View):
    def get(self, request):
        contacts = Person.objects.all().order_by('name')
        form = PersonForm()
        return render(request, 'contacts_contact_list.html', {'form': form, 'contacts': contacts})

    def post(self, request):
        form = PersonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Contact has been created.')
            return redirect('contactlist-contact_list')
        else:
            messages.error(request, 'While adding new contact an error has occurred.')
            return redirect('contactlist-contact_list')


