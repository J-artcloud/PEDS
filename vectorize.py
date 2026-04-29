# ── Vocabulary building and text vectorisation ────────────────────────────────
from dataset import get_all_emails


def build_vocabulary() -> list:
    """
    Build a sorted, stable vocabulary list from the email dataset.

    Fix 1 – Returns a SORTED LIST, not a set.
             A set has no guaranteed order; calling build_vocabulary() twice
             could yield a different word order each time, making vectors from
             training completely incompatible with vectors from prediction.
    Fix 2 – Removed debug print(type(vocab)) and module-level execution code.
    """
    emails = get_all_emails()
    vocab = set()
    for email in emails:
        words = email["subject"].lower().split() + email["body"].lower().split()
        vocab.update(words)
    return sorted(vocab)          # sorted list → consistent, reproducible order


def text_to_vector(text: str, vocab: list) -> list:
    """
    Convert a text string into a bag-of-words count vector aligned to vocab.

    Fix – The function now USES the vocab parameter it receives instead of
          silently rebuilding it internally (which was both wasteful and
          dangerous when vocab order is not stable).
    """
    words = text.lower().split()
    return [words.count(word) for word in vocab]
