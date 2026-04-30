
from dataset import get_all_emails


def build_vocabulary():
    """
    Builds a vocabulary list from the emails in dataset
    Vars:
        emails: list of all emails in dataset
        vocab: set of unique vocabulary in words
    
        returns: 
            sorted list of vocabulary
    """

    emails = get_all_emails()
    vocab = set()
    for email in emails:
        words = email["subject"].lower().split() + email["body"].lower().split()
        vocab.update(words)
    return sorted(vocab)    

# Convert text to a vector based on the vocabulary
def text_to_vector(text: str, vocab: list):
    """
    returns a list of occurances for each word in vocabulary in text

    Args: 
        text:  all text from user that is subject + body
        vocab: list of vocabulary words

    Vars: 
        words: list of words in text
    
    Return:
        returns a list of nummbers which contains the number of occurences of each word in vocab
        in words
    
    """
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
