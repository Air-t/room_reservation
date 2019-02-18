from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from contacts.forms import PersonForm
from contacts.models import Person


class ContactList(View):
    def get(self, request):
        contacts = Person.objects.all().order_by('surname')
        form = PersonForm()
        return render(request, 'contact_list.html', {'form': form, 'contacts': contacts})

    def post(self, request):
        if request.POST.get('action') == 'delete':
            person = Person.objects.get(pk=int(request.POST.get('id')))
            person.delete()
            messages.success(request, 'Contact deleted.')
            return redirect('contactlist-contact_list')

        form = PersonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Contact has been created.')
            return redirect('contactlist-contact_list')
        else:
            messages.error(request, 'While adding new contact an error has occurred.')
            return redirect('contactlist-contact_list')


class ModifyPerson(View):
    def get(self, request, id):
        pass

    def post(self, request):
        pass


class ViewPerson(View):
    def get(self, request, id):
        person = Person.objects.get(pk=id)
        form = PersonForm(instance=person)
        return render(request, 'contact_details.html', {'contact': person, 'form': form})

    def post(self, request, id):
        pass