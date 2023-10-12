from django.shortcuts import render, redirect
from .forms import TextDataForm
from django.http import HttpResponse

def index(request):
    return render(request, 'shop/index.html')

def index(request):
    return render(request,'shop/login.html')


def save_text(request):
    if request.method == 'POST':
        form = TextDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirect to a success page or any other page
    else:
        form = TextDataForm()
    return render(request, 'shop/index.html', {'form': form})
