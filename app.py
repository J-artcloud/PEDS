import base64
import os
import streamlit as st

from dataset import get_all_emails
from Run_engine import analyse
from ML_model import train, predict, LABELS
from vectorize import text_to_vector, build_vocabulary


st.set_page_config(
    page_title="PEDS - Phishing Email Detection System",
    page_icon="🛡️",
    layout="centered",
)


# ── Background styling ────────────────────────────────────────────────────────

def _set_background(image_path: str) -> None:
    if not os.path.exists(image_path):
        st.warning(f"Background image not found at: {image_path}")
        return

    with open(image_path, "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode()

    css = f"""
    <style>
    [data-testid="stAppViewContainer"] {{
        background-image      : url("data:image/jpeg;base64,{encoded}") !important;
        background-size       : cover !important;
        background-position   : center !important;
        background-repeat     : no-repeat !important;
        background-attachment : fixed !important;
    }}
    body, .stApp {{
        background-image      : url("data:image/jpeg;base64,{encoded}") !important;
        background-size       : cover !important;
        background-position   : center !important;
        background-repeat     : no-repeat !important;
        background-attachment : fixed !important;
    }}
    [data-testid="stMain"],
    [data-testid="stMainBlockContainer"],
    [data-testid="stBottom"],
    [data-testid="stHeader"],
    [data-testid="stToolbar"],
    [data-testid="stDecoration"],
    section.main,
    .main .block-container,
    .block-container {{
        background-color : transparent !important;
        background-image : none !important;
    }}
    .block-container {{
        background-color        : rgba(5, 10, 25, 0.75) !important;
        border-radius           : 18px !important;
        padding                 : 2.5rem 2.5rem 2rem !important;
        backdrop-filter         : blur(4px) !important;
        -webkit-backdrop-filter : blur(4px) !important;
        border                  : 1px solid rgba(0, 212, 255, 0.15) !important;
    }}
    h1, h2, h3, h4, p, label, .stMarkdown {{ color: #e8f4f8 !important; }}
    .stTextInput > div > div > input,
    .stTextArea  > div > div > textarea {{
        background-color : rgba(10, 20, 40, 0.80) !important;
        color            : #c8e6f5 !important;
        border           : 1px solid rgba(0, 212, 255, 0.35) !important;
        border-radius    : 8px !important;
    }}
    .stButton > button {{
        background    : linear-gradient(135deg, #0077b6, #00b4d8);
        color         : #ffffff;
        font-weight   : 700;
        font-size     : 1.05rem;
        border        : none;
        border-radius : 10px;
        padding       : 0.6rem 2.2rem;
        transition    : all 0.2s ease;
        width         : 100%;
    }}
    .stButton > button:hover {{
        background : linear-gradient(135deg, #00b4d8, #90e0ef);
        color      : #023e8a;
        transform  : translateY(-2px);
        box-shadow : 0 6px 20px rgba(0, 180, 216, 0.45);
    }}
    [data-testid="stExpander"] {{
        background-color : rgba(0, 119, 182, 0.25) !important;
        border-radius    : 8px !important;
    }}
    [data-testid="stExpander"] summary {{ color: #90e0ef !important; }}
    section[data-testid="stSidebar"] {{ background-color: rgba(5, 10, 25, 0.85); }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)


_set_background("background.jpeg")


#Model loading (cached so it only trains once per session) 

@st.cache_resource
def load_model() -> tuple[dict, list]:
    """
    Train the ML model and cache the result.

    Fix – Previously returned (train, predict) — the function objects themselves!
          Now correctly calls train() and returns (prototype_dict, vocab).
    """
    prototype_dict, vocab = train()   # actually call train()
    return prototype_dict, vocab


prototype_dict, vocab = load_model()


# Page header 
st.markdown(
    """
    <div style='text-align:center; padding-bottom:0.5rem;'>
        <h1 style='font-size:2.3rem; margin:0; letter-spacing:1px;
                   color:#90e0ef !important;'>Phishing Email Detection System</h1>
        <p style='color:#caf0f8 !important; font-size:1.05rem; margin-top:0.3rem;'>
            AI-powered phishing email detection — Cyber Security + Machine Learning
        </p>
    </div>
    <hr style='border-color:rgba(0,212,255,0.2); margin-bottom:1.5rem;'>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <p>
        <b style='color:#00d4ff;'>What is a phishing email?</b>
        <br>A <b>phishing email</b> is a <b>fake message</b> designed to trick you
        into clicking a <b>harmful link</b> or handing over your personal information.
    </p>
    <p>
        <b style='color:#00d4ff;'>PEDS</b> is a system designed to pinpoint these
        emails. It analyses your email and tells you how legitimate it is.
    </p>
    """,
    unsafe_allow_html=True,
)

st.markdown("#### Paste the email you want to analyse")

subject = st.text_input(
    "Subject line",
    placeholder="e.g. URGENT: Your account has been suspended",
)
body = st.text_area(
    "Email body",
    placeholder="Paste the full email body here...",
    height=160,
)

st.markdown("---")

# Analysis logic 
if st.button("🔍  Check This Email"):

    if not subject.strip() and not body.strip():
        st.warning(" Please enter a subject line or body before analysing.")

    else:
        #Rule-based engine 
        rule_result = analyse(subject, body)
        rule_score  = rule_result["risk_score"]
        rule_label  = rule_result["label"]   # now a plain Title-Case string

        # ML model (called ONCE; result reused below) 
        ml_label, ml_scores = predict(subject, body, prototype_dict, vocab)

        # ── Hybrid decision ──
        # Trust the rule engine when it is very confident (clear safe or clear threat).
        # Fall back to ML for the ambiguous middle ground.
        if rule_score == 0 or rule_score >= 4:
            final_label = rule_label
        else:
            final_label = ml_label

        # ── Verdict banner ──
        st.markdown("### Final Verdict")

        if final_label == "Legitimate":
            st.success("**LEGITIMATE** — This email does not appear to be a threat.")
        elif final_label == "Suspicious":
            st.warning(" **SUSPICIOUS** — This email shows some warning signs. Proceed with caution.")
        else:
            st.error("**PHISHING** — This email is likely a phishing attempt. Do NOT click any links!")

        st.markdown(
            f"<small style='color:#a0c4d8;'>Rule label: <b>{rule_label}</b> "
            f"(score {rule_score}) &nbsp;|&nbsp; ML label: <b>{ml_label}</b></small>",
            unsafe_allow_html=True,
        )

        st.markdown("---")
        st.markdown("**ML confidence scores (higher = more similar to that class):**")

        # ── Score bars ──
        # Fix – ml_scores is a list aligned to LABELS ["Legitimate","Suspicious","Phishing"]
        #       Previously the loop iterated over the return tuple itself (wrong),
        #       used dict.update() which always returns None, and set lbl = {} (a dict!).

        ICONS   = {"Legitimate": "", "Suspicious": "",  "Phishing": ""}
        COLOURS = {"Legitimate": "#55cc73", "Suspicious": "#f3cd73", "Phishing": "#da4052"}

        max_score = max(ml_scores) if max(ml_scores) > 0 else 1   # avoid div-by-zero

        for lbl, score in zip(LABELS, ml_scores):
            icon   = ICONS[lbl]
            colour = COLOURS[lbl]
            pct    = min(int((score / max_score) * 100), 100)

            st.markdown(
                f"""
                <div style='margin-bottom:0.6rem;'>
                    <span style='color:{colour}; font-weight:700;'>{icon} {lbl}</span>
                    &nbsp;&nbsp;
                    <span style='color:#caf0f8;'>{score:.4f}</span>
                    <div style='background:rgba(255,255,255,0.1); border-radius:6px;
                                height:10px; margin-top:4px;'>
                        <div style='background:{colour}; width:{pct}%; height:10px;
                                    border-radius:6px;'></div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )


#Footer 
st.markdown(
    """
    <hr style='border-color:rgba(0,212,255,0.1); margin-top:2rem;'>
    <p style='text-align:center; color:rgba(200,230,245,0.45); font-size:0.78rem;'>
        PEDS · Built with Python & Streamlit · Cybersecurity + ML Capstone Project
    </p>
    """,
    unsafe_allow_html=True,
)
