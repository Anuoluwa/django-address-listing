from django.shortcuts import render
from django.views import generic
from .models import Contact

# Create your views here.

class ContactListView(generic.ListView):
    model = Contact

class ContactDetailView(generic.DetailView):
    model = Contact

def index(request):
    return render(request,'index.html')

def add(request):
    return render(request,'add.html')
