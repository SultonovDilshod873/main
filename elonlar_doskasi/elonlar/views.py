from django.shortcuts import render, redirect
from .models import Elon
from .forms import ElonForm

def elon_list(request):
    elonlar = Elon.objects.all()
    return render(request, 'elonlar/elon_list.html', {'elonlar': elonlar})

def elon_create(request):
    if request.method == 'POST':
        form = ElonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('elon_list')
    else:
        form = ElonForm()
    return render(request, 'elonlar/elon_form.html', {'form': form})
        
