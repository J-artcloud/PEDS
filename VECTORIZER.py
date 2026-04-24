
from dataset import get_all_emails

emails = get_all_emails()


# Build a vocabulary from the email dataset
def build_vocabulary():
    vocab = set()
    for email in emails:
        words = email["subject"].lower().split() + email["body"].lower().split()
        vocab.update(words)
    return list(vocab)

# Convert text to a vector based on the vocabulary
def text_to_vector(text, vocab):
    vector = []
    words = text.lower().split()
    for word in vocab:
        count = 0
        if word in words:
            count = words.count(word)
            vector.append(count)
        else:
            vector.append(0)
    return vector

vocabulary = build_vocabulary()
