# Gmail Authentication Troubleshooting

## Current Issue
Gmail is rejecting the app password with "Username and Password not accepted" error.

## Solutions to Try

### 1. Generate New App Password
1. Go to: https://myaccount.google.com/apppasswords
2. Make sure 2FA is enabled first
3. Generate a NEW app password (don't reuse the old one)
4. Name it "Portfolio Contact 2"
5. Copy the 16-character password
6. Update .env file: EMAIL_HOST_PASSWORD=new-password-without-spaces

### 2. Check Google Account Security
1. Go to: https://myaccount.google.com/security
2. Make sure "Less secure app access" is ON (if available)
3. Check if Google is blocking suspicious sign-ins

### 3. Alternative: Use SendGrid (Recommended for Production)
1. Sign up for SendGrid (free tier available)
2. Get API key
3. Update settings to use SendGrid backend

### 4. Alternative: Use Outlook/Hotmail
1. Create a new Outlook email
2. Use SMTP settings:
   - EMAIL_HOST = 'smtp-mail.outlook.com'
   - EMAIL_PORT = 587

## Current Status
- Contact form works perfectly (verified in console mode)
- Email content generates correctly
- Only Gmail authentication is failing

## Next Steps
1. Try generating a fresh app password
2. If still fails, consider switching to SendGrid or Outlook
3. Console mode works for testing in the meantime
