import os
from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

def home(request):
    return render(request, 'main/home.html')

def contact(request):

    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        message = request.POST.get('message', '').strip()
        
        # Basic validation
        if not name or not email or not message:
            messages.error(request, 'All fields are required.')
            return render(request, 'main/contact.html')
        
        if len(name) < 2:
            messages.error(request, 'Name must be at least 2 characters long.')
            return render(request, 'main/contact.html')
        
        if len(message) < 10:
            messages.error(request, 'Message must be at least 10 characters long.')
            return render(request, 'main/contact.html')

        try:
            send_mail(
                subject=f'Portfolio Contact from {name}',
                message=f'From: {name}\nEmail: {email}\n\nMessage:\n{message}',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.EMAIL_HOST_USER],
                fail_silently=False,
            )
            messages.success(request, 'Your message has been sent successfully! You will receive a response shortly.')
        except Exception as e:
            print(f'EMAIL ERROR: {e}')
            messages.error(request, f'Error sending message: {e}. Please try again later.')

    return render(request, 'main/contact.html')