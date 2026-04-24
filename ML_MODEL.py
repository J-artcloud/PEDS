# Train model and make predictions


from dataset import get_all_emails
from VECTORIZER import text_to_vector, vocabulary

def dot_product(v1, v2):
    sum = 0
    for num1, num2 in zip(v1, v2):
        sum += num1 * num2
    return sum

def train():
    emails = get_all_emails()
    
    groups = {}
    
    label_vectors = {}
    
    legitimate_emails =[]
    phising_emails = []
    suspicious_emails = []

    prototype = []
    
    # group emails by lable
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
    

    # covert email to vector
    for label in groups:
        label_list = []
        for email in groups[label]:
            text = email["subject"].lower() + " " + email["body"].lower()
            label_list.append(text_to_vector(text, vocabulary))
        label_vectors[label] = label_list
    
    # averaging into one vector prototype
    

        
train()





















