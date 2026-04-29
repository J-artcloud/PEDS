# ── Prototype-based nearest-centroid classifier ───────────────────────────────
from dataset import get_all_emails
from vectorize import text_to_vector, build_vocabulary

# Class labels in a fixed order so index → label mapping is always consistent
LABELS = ["Legitimate", "Suspicious", "Phishing"]


def dot_product(v1: list, v2: list) -> float:
    """Compute the dot product of two equal-length vectors."""
    return sum(a * b for a, b in zip(v1, v2))


def train() -> tuple[dict, list]:
    """
    Train the prototype (nearest-centroid) classifier.

    Returns:
        prototype_dict : {label: prototype_vector}
        vocab          : the vocabulary list used (must be reused at predict time)

    Fix 1 – "Phising" typo corrected to "Phishing" everywhere.
    Fix 2 – vocab is built ONCE here and returned so predict() reuses the
             exact same vocab (same order = compatible vectors).
    Fix 3 – train() no longer calls itself or rebuilds vocab mid-loop.
    """
    emails = get_all_emails()
    vocab = build_vocabulary()          # built once; returned for reuse

    # Group emails by label
    groups: dict[str, list] = {lbl: [] for lbl in LABELS}
    for email in emails:
        label = email["label"]
        if label in groups:
            text = email["subject"].lower() + " " + email["body"].lower()
            groups[label].append(text_to_vector(text, vocab))

    # Compute one prototype vector per class (element-wise mean)
    prototype_dict = {}
    for label, vectors in groups.items():
        if not vectors:
            continue
        dim = len(vocab)
        total = [0.0] * dim
        for vec in vectors:
            for i, val in enumerate(vec):
                total[i] += val
        prototype_dict[label] = [x / len(vectors) for x in total]

    return prototype_dict, vocab


def predict(subject: str, body: str,
            prototype_dict: dict, vocab: list) -> tuple[str, list]:
    """
    Predict the label for a new email.

    Returns:
        (label_string, scores_list)
        where scores_list is aligned to LABELS order.

    Fix 1 – No longer calls train() internally (was re-training on every click).
    Fix 2 – Uses the passed-in vocab and prototype_dict correctly.
    Fix 3 – Passes vocab (the list) to text_to_vector, not build_vocabulary
             (the function object) – this was causing a TypeError crash.
    Fix 4 – "Phising" typo corrected to "Phishing".
    """
    text = subject.lower() + " " + body.lower()
    vector = text_to_vector(text, vocab)        # vocab is the list, not the function

    scores = []
    for label in LABELS:
        if label in prototype_dict:
            scores.append(dot_product(vector, prototype_dict[label]))
        else:
            scores.append(0.0)

    best_index = scores.index(max(scores))
    return LABELS[best_index], scores
