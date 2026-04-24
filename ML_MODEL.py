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
    for label in label_vectors:
        prototype_vector = [0] * len(vocabulary)
        for vector in label_vectors[label]:
            for i in range(len(vector)):
                prototype_vector[i] += vector[i]
        prototype_vector = [x / len(label_vectors[label]) for x in prototype_vector]
        prototype.append(prototype_vector)
    
    # dictionary to store the prototype vector for each label
    prototype_dict = {}
    for i, label in enumerate(label_vectors):
        prototype_dict[label] = prototype[i]
        print(label)
    return prototype_dict

def predict(subject, body, prototype_dict, vocab):
    # converting new email to vectors 
    text = subject.lower() + " " + body.lower()
    vector = text_to_vector(text, vocab)
    
    # computing dot prod for each lable
    prototype_dict = train()
    scores = []
    for label in prototype_dict:
        score = dot_product(vector, prototype_dict[label])
        scores.append(score)
    max_score = max(scores)
    
    # selecting which label has the highest score
    if max_score == scores[0]:
        return "Legitimate", scores
    elif max_score == scores[1]:
        return "Suspicious", scores
    else:   
        return "Phising", scores
