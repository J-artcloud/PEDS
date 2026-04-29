# ── Rule-based phishing detection engine ──────────────────────────────────────
# Keywords are defined FIRST so analyse() can safely reference them.

PHISHING_KEYWORDS = [
    "urgent", "verify", "suspended", "click here", "prize", "password",
    "winner", "confirm", "immediately", "account locked", "update your details",
    "login now", "security alert", "unusual activity", "act now", "limited time",
    "free", "claim now", "reset password", "bank details", "ssn", "credit card",
    "payment failed", "verify your identity", "access denied",
]


def analyse(subject: str, body: str) -> dict:
    """
    Rule-based analysis of an email.

    Returns:
        {
            "risk_score": int,
            "label": "Legitimate" | "Suspicious" | "Phishing"
        }

    Fix 1 – PHISHING_KEYWORDS moved above this function.
    Fix 2 – Labels now use Title-Case so app.py comparisons work.
    Fix 3 – Return dict contains the plain category name, not a sentence.
    Fix 4 – Risk-score branches now cover every possible integer without gaps.
    """
    risk_score = 0
    message = (subject + " " + body).lower()

    # Keyword check
    for keyword in PHISHING_KEYWORDS:
        if keyword in message:
            risk_score += 1

    # ALL-CAPS word check (more than 3 all-caps words is suspicious)
    caps_count = sum(1 for word in (subject + " " + body).split() if word.isupper())
    if caps_count > 3:
        risk_score += 1

    # Unsafe HTTP link (not HTTPS) is a strong phishing signal
    if "http://" in body:
        risk_score += 2

    # ── Label assignment (no gaps in coverage) ──
    if risk_score <= 1:
        label = "Legitimate"
    elif risk_score <= 3:          # covers 2 and 3 (was missing 2 before)
        label = "Suspicious"
    else:                          # 4 and above
        label = "Phishing"

    return {"risk_score": risk_score, "label": label}
