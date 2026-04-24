def get_all_emails():
    Emails = [
        {"subject": "Your order has shipped",
         "body": "Thank you for shopping with us. Your order #12345 will arrive soon.",
         "label": "Legitimate"},

        {"subject": "Monthly statement ready",
         "body": "Dear customer, your monthly bank statement is ready to view online.",
         "label": "Legitimate"},

        {"subject": "Meeting reminder",
         "body": "This is a reminder for our meeting tomorrow at 10 AM. Regards, HR team.",
         "label": "Legitimate"},

        {"subject": "Invoice #7890 attached",
         "body": "Please find your invoice attached. Thank you for your payment.",
         "label": "Legitimate"},

        {"subject": "Your subscription has been renewed",
         "body": "Your subscription to Streamly has been successfully renewed. Thank you.",
         "label": "Legitimate"},

        {"subject": "Flight ticket confirmation",
         "body": "Your flight to New York is confirmed. Ticket number: NY123456.",
         "label": "Legitimate"},

        {"subject": "Password changed successfully",
         "body": "Your account password has been updated. If this wasn't you, contact support.",
         "label": "Legitimate"},

        # -------------------- SUSPICIOUS --------------------
        {"subject": "You may have won a gift card",
         "body": "Congratulations! Please confirm your details to claim your prize.",
         "label": "Suspicious"},

        {"subject": "Verify your account information",
         "body": "We noticed unusual activity. Please update your account details to continue.",
         "label": "Suspicious"},

        {"subject": "Limited time offer!",
         "body": "You have been selected for a special promotion. Click to find out more.",
         "label": "Suspicious"},

        {"subject": "Claim your reward now",
         "body": "Hello! We noticed you qualify for a reward. Confirm your information today.",
         "label": "Suspicious"},

        {"subject": "Your account needs verification",
         "body": "Please verify your account information to avoid restrictions.",
         "label": "Suspicious"},

        {"subject": "Congratulations, you won!",
         "body": "You've been chosen for a surprise gift. Confirm your email to claim.",
         "label": "Suspicious"},

        {"subject": "Action required: Update your info",
         "body": "Your account might be at risk. Please provide the requested information.",
         "label": "Suspicious"},

        # -------------------- PHISHING --------------------
        {"subject": "URGENT: Verify your account NOW",
         "body": "Click here immediately http://bad-link.com or your account will be closed!",
         "label": "Phishing"},

        {"subject": "Your account has been suspended",
         "body": "Provide your password to reactivate your account immediately.",
         "label": "Phishing"},

        {"subject": "WINNER! Claim your $1000 prize",
         "body": "You are selected! Visit http://fake-prize.com and enter your personal info now.",
         "label": "Phishing"},

        {"subject": "Confirm your banking details",
         "body": "We detected suspicious activity. Login here http://fake-bank.com to confirm.",
         "label": "Phishing"},

        {"subject": "Immediate action required",
         "body": "Your identity must be verified. Send your SSN and password immediately.",
         "label": "Phishing"},

        {"subject": "Attention! Your payment failed",
         "body": "Click the link http://fake-payments.com to update your payment info to avoid closure.",
         "label": "Phishing"},
    ]
    return Emails

