import os
from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

def home(request):
    return render(request, 'main/home.html')

def contact(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        try:
            send_mail(
                subject=f'Portfolio Contact from {name}',
                message=f'From: {name}\nEmail: {email}\n\nMessage:\n{message}',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.EMAIL_HOST_USER],
            )
            messages.success(request, 'Your message has been sent successfully! You will receive a response shortly.')
        except Exception as e:
            print(f'EMAIL ERROR: {e}')
            messages.error(request, f'Error: {e}')

    return render(request, 'main/contact.html')