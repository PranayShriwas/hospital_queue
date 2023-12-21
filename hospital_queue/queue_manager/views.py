from django.shortcuts import render, redirect
from .models import Patient

def index(request):
    patients = Patient.objects.order_by('-urgency', 'timestamp')
    return render(request, 'index.html', {'patients': patients})

def add_pat(request):
    return render(request,'addpasitent.html')

def add_patient(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        urgency = request.POST.get('urgency')
        Patient.objects.create(name=name, urgency=urgency)
    return redirect('/')

