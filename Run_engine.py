from dataset import get_all_emails
emails = get_all_emails()

def analyse(subject,body):
    risk_score = 0
    caps_count = 0
    # phishing words check #
    message = subject + " " + body
    for word in PHISHING_KEYWORDS:
        if word in message.lower():
            risk_score += 1
    # capitalised words check
    for word in message.split(" "):
        if word.isupper():
            caps_count += 1
    if caps_count > 3:
        risk_score+=1
    # unsafe link check
    if "http://" in body:
        risk_score+=2
    # email label determination
    if risk_score<=1:
        label="legitimate"
    elif risk_score<=3:
        label="suspicious"
    else:
        label="phishing"
    # final output to be displayed
    return {"risk_score": risk_score, "label":f"this email is a {label} email" }


PHISHING_KEYWORDS= [ "urgent","verify","suspended","click here","prize","password","winner","confirm","immediately",
    "account locked","update your details","login now","security alert","unusual activity","act now","limited time",
    "free","claim now","reset password","bank details","ssn","credit card","payment failed","verify your identity",
    "access denied"]
for email in emails:
    subject = email["subject"]
    body = email["body"]
    result=analyse(subject,body)
    print(result)