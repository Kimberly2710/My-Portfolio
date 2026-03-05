from django.shortcuts import render
from django.contrib import messages

def home(request):
    return render(request, 'main/home.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        messages.success(request, f'Thanks {name}! Your message has been received.')
        return render(request, 'main/contact.html')
    return render(request, 'main/contact.html')