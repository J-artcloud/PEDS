# Train model and make predictions


from dataset import get_all_emails
#from VECTORIZER import text_to_vector

def dot_product(v1, v2):
    sum = 0
    for num1, num2 in zip(v1, v2):
        sum += num1 * num2
    return sum

def train():
    emails = get_all_emails()
    groups = {}
    legitimate_emails =[]
    phising_emails = []
    suspicious_emails = []
    
    for email in emails:
        if email["label"] == "Legitimate":
            legitimate_emails.append(email)
            groups["Legitimate"] = legitimate_emails
        elif email["label"] == "Suspicious":
            suspicious_emails.append(email)
            groups["Suspicious"] = suspicious_emails
        else:
            phising_emails.append(email)
            groups["Phising"] =  phising_emails
train()