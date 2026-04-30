# Train model and make predictions


from dataset import get_all_emails
from VECTORIZER import text_to_vector, build_vocabulary

def dot_product(v1: list, v2: list):
    """
    function return the dot product of two vectors
    """
    return sum(x * y for x, y in zip(v1, v2))

def train() -> tuple[dict, list]:
    
    emails = get_all_emails()
    vocab = build_vocabulary()





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
