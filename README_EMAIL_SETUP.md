# Email Configuration Setup

## Development Mode (Current Setup)
The portfolio is currently configured to use Django's console email backend, which prints emails to the console instead of actually sending them. This is perfect for testing.

## Production Setup
To actually send emails in production, you'll need to:

1. Update EMAIL_BACKEND in settings.py:
   ```python
   EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
   ```

2. Configure your email provider settings:
   ```python
   EMAIL_HOST = 'smtp.gmail.com'  # or your provider
   EMAIL_PORT = 587
   EMAIL_USE_TLS = True
   EMAIL_HOST_USER = 'your-email@gmail.com'
   EMAIL_HOST_PASSWORD = 'your-app-password'
   ```

3. For Gmail, you'll need to:
   - Enable 2-factor authentication
   - Generate an app password
   - Use the app password instead of your regular password

## Testing the Contact Form
1. Navigate to http://127.0.0.1:8000/contact/
2. Fill out the form with test data
3. Check the Django server console for the email output
4. You should see the email content printed in the console

## Email Validation
The contact form now includes:
- Required field validation
- Minimum length validation (name: 2 chars, message: 10 chars)
- Proper error handling and user feedback
- Different styling for success (green) and error (red) messages
