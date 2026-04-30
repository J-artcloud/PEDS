# Train model and make predictions


from dataset import get_all_emails
from VECTORIZER import text_to_vector, build_vocabulary


LABELS = ["Legitimate", "Suspicious", "Phishing"]


def dot_product(v1: list, v2: list):
    """function return the dot product of two vectors"""
    return sum(x * y for x, y in zip(v1, v2))


def train() -> tuple[dict, list]:
    """
    Trains prototype
    Returns
    -------
        tuple[dict, list]
        returns a tuple containing the prototype dictionary and the vocabulary

    """
    
    emails = get_all_emails()
    vocab = build_vocabulary()
    
    # grouping email by label and covert each email to vector
    groups = {lbl: [] for lbl in LABELS}
    for email in emails:
        label = email["label"]
        if label in groups:
            text = email["subject"].lower() + " " + email["body"].lower()
            groups[label].append(text_to_vector(text, vocab))
    
    # averaging all vectors into one prototype vector
    prototype_dict = {}
    for label, vectors in groups.items():
        if not vectors:
            continue
        dimension = len(vocab)
        total = [0.0] * dimension
        for vector in vectors:
            for idx, val in enumerate(vector):
                total[idx] += val
        prototype_dict[label] = [val / len(vectors) for val in total]
    
    return prototype_dict, vocab
            
            



def predict(subject: str, body: str, prototypes, vocab: list) -> tuple[str, list]:
    """
    function predicts the label for any given email

    Args: 
        subject: text subject from email
        body: text body from email
        prototypes: prototype dictionary
        vocab: vocabulary
    
    returns:
        function returns the label whose prototype has the highest dot product score
        along with the scores
    """
    prototypes, vocab  = train()
    text = subject.lower()+ " " + body.lower()
    vector = text_to_vector(text, vocab)

    scores = []
    for label in LABELS:
        if label in prototypes:
            scores.append(dot_product(vector, prototypes[label]))
        else:
            scores.append(0.0)
    best_score_index = scores.index(max(scores))

    return LABELS[best_score_index], scores
