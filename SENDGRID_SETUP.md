# SendGrid Email Setup Guide

## Why SendGrid?
- More reliable than Gmail for applications
- Professional email delivery service
- Free tier available (100 emails/day)
- Better deliverability rates

## Setup Steps

### 1. Create SendGrid Account
1. Go to https://signup.sendgrid.com/
2. Sign up for free account
3. Verify your email address

### 2. Verify Your Domain (Optional but Recommended)
1. Go to SendGrid Dashboard → Settings → Sender Authentication
2. Add your domain (or use single sender verification)
3. Complete DNS verification

### 3. Create API Key
1. Go to Settings → API Keys
2. Click "Create API Key"
3. Select "Restricted Access"
4. Give it permissions: Mail Send → Full Access
5. Copy the API key

### 4. Update .env File
Replace `your-sendgrid-api-key-here` with your actual API key:
```
SENDGRID_API_KEY=SG.your-actual-api-key-here
```

### 5. Test the Contact Form
1. Restart the Django server
2. Go to /contact/ and submit a test message
3. Check your Gmail inbox for the email

## Current Configuration
- Backend: SMTP SendGrid
- From: noreply@yourportfolio.com
- To: vinlawz07@gmail.com
- Host: smtp.sendgrid.net:587

## Alternative: Quick Single Sender Verification
If you don't want to verify a domain:
1. Go to SendGrid Dashboard → Settings → Single Sender Verification
2. Add your email (vinlawz07@gmail.com) as sender
3. Update the from_email in views.py to your email

## Benefits
✅ Reliable email delivery
✅ Professional appearance
✅ Better spam filter avoidance
✅ Detailed delivery reports
✅ Free tier sufficient for portfolio
