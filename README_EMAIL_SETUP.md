# Email Configuration Setup

## Current Configuration
The portfolio is configured to send emails through Gmail using your email: vinlawz07@gmail.com

## Setup Steps for Gmail

### 1. Enable 2-Factor Authentication
- Go to https://myaccount.google.com/security
- Enable 2-Factor Authentication for your Gmail account

### 2. Generate App Password
- Go to https://myaccount.google.com/apppasswords
- Select "Mail" for the app
- Select "Other (Custom name)" and name it "Portfolio Contact"
- Copy the 16-character password generated

### 3. Create .env File
Create a `.env` file in the project root with:
```
SECRET_KEY=django-insecure-development-key-for-portfolio-only
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=vinlawz07@gmail.com
EMAIL_HOST_PASSWORD=your-16-character-app-password
```

### 4. Test the Contact Form
1. Navigate to http://127.0.0.1:8000/contact/
2. Fill out the form with test data
3. You should receive an email in your Gmail inbox

## Alternative: Console Mode (for testing)
If you want to test without sending real emails, set:
```
EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
```
This will print emails to the console instead.

## Email Validation
The contact form includes:
- Required field validation
- Minimum length validation (name: 2 chars, message: 10 chars)
- Proper error handling and user feedback
- Different styling for success (green) and error (red) messages
