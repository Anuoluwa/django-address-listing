from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Contact

# Create your views here.

class ContactListView(generic.ListView):
    model = Contact
    paginate_by = 20

class ContactDetailView(generic.DetailView):
    model = Contact

def index(request):
    return render(request,'index.html')


class ContactCreate(CreateView):
    model = Contact
    fields = '__all__'
    success_url = reverse_lazy('contacts')

class ContactUpdate(UpdateView):
    model = Contact
    fields = '__all__'
    success_url = reverse_lazy('contacts')


class ContactDelete(DeleteView):
    model = Contact
    """
        reverse_lazy() is a lazily executed version of reverse(), used because I am providing
        a URL to a class-based view attribute.
    """
    success_url = reverse_lazy('contacts')
