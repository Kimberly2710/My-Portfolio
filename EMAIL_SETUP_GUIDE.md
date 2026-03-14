# Email Configuration Guide for Developers

## Quick Setup for Any Email Provider

### Step 1: Update Email Settings
Edit `portfolio/settings.py` and modify these lines:

```python
# Email configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'your-smtp-server.com'     # Your email provider's SMTP server
EMAIL_PORT = 587                         # Usually 587 for TLS
EMAIL_USE_TLS = True                       # Usually True
EMAIL_HOST_USER = 'your-email@domain.com'   # Your email address
EMAIL_HOST_PASSWORD = 'your-app-password'     # Your email password/app password
```

### Step 2: Update Recipient Email
Edit `main/views.py` and change this line:

```python
recipient_list=['your-email@domain.com'],  # Change to your email
```

### Popular Email Providers

#### Gmail
```python
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
# Note: Must use App Password, not regular password
```

#### Outlook/Hotmail
```python
EMAIL_HOST = 'smtp-mail.outlook.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
```

#### Yahoo Mail
```python
EMAIL_HOST = 'smtp.mail.yahoo.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
# Note: Must use App Password
```

#### Custom Domain Email
```python
EMAIL_HOST = 'mail.yourdomain.com'  # Check with your hosting provider
EMAIL_PORT = 587
EMAIL_USE_TLS = True
```

### Step 3: Test the Configuration
1. Restart Django server: `python manage.py runserver`
2. Go to `/contact/` and submit a test message
3. Check your email inbox

### Security Best Practices

#### For Gmail Users:
1. Enable 2-Factor Authentication
2. Generate App Password: https://myaccount.google.com/apppasswords
3. Use app password, not regular password

#### For All Users:
- Never commit passwords to Git
- Use environment variables for production
- Consider using email services like SendGrid for production

### Environment Variables (Recommended for Production)

Create `.env` file:
```
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

Update `settings.py`:
```python
import os
from dotenv import load_dotenv
load_dotenv()

EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_PORT = int(os.getenv('EMAIL_PORT', 587))
EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS', 'True') == 'True'
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
```

### Troubleshooting

#### Common Errors:
1. **"Username and Password not accepted"**
   - Check app password generation
   - Verify 2FA is enabled
   - Ensure correct SMTP server

2. **"Connection refused"**
   - Check SMTP server address
   - Verify port number
   - Check firewall settings

3. **"SSL/TLS error"**
   - Try EMAIL_USE_TLS = False
   - Try different port (465 for SSL)

### Quick Copy-Paste Templates

#### Gmail Template:
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-16-character-app-password'
```

#### Outlook Template:
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp-mail.outlook.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@outlook.com'
EMAIL_HOST_PASSWORD = 'your-regular-password'
```

That's it! Other developers can now easily configure their own email by following these steps.
