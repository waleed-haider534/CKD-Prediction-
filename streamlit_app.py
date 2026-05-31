import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="CKD Prediction System",
    page_icon="🫘",
    layout="wide"
)

# Custom CSS for clean light theme
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

    * {
        font-family: 'Inter', sans-serif !important;
    }

    /* Light background */
    .stApp {
        background: #fafafa;
    }

    /* Header styling */
    .custom-header {
        background: linear-gradient(135deg, #2563eb 0%, #1e40af 100%);
        padding: 30px;
        border-radius: 16px;
        text-align: center;
        margin-bottom: 24px;
    }

    .custom-header h1 {
        color: white;
        font-size: 2.2rem;
        font-weight: 700;
        margin-bottom: 8px;
    }

    .custom-header p {
        color: rgba(255,255,255,0.9);
        font-size: 1rem;
    }

    /* Card styling */
    .form-card {
        background: white;
        border-radius: 16px;
        padding: 24px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        border: 1px solid #e5e7eb;
        margin-bottom: 20px;
    }

    /* Section headers */
    .section-title {
        font-size: 1.3rem;
        font-weight: 700;
        color: #111827;
        margin-bottom: 20px;
        padding-bottom: 10px;
        border-bottom: 2px solid #e5e7eb;
    }

    /* Input fields - blood test results */
    .stNumberInput input {
        background-color: #ffffff !important;
        color: #000000 !important;
        border: 2px solid #d1d5db !important;
        border-radius: 10px !important;
        font-weight: 500 !important;
    }

    .stNumberInput input:focus {
        border-color: #2563eb !important;
        box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.15) !important;
    }

    /* Ensure labels are visible */
    .stNumberInput label {
        color: #374151 !important;
        font-weight: 600 !important;
        font-size: 0.9rem !important;
    }

    /* Input field container */
    .stNumberInput > div {
        background-color: #ffffff !important;
    }

    .stNumberInput > div > div {
        background-color: #ffffff !important;
    }

    /* Selectbox styling */
    .stSelectbox label {
        color: #374151 !important;
        font-weight: 600 !important;
    }

    .stSelectbox div[data-baseweb="select"] {
        background: white !important;
    }

    .stSelectbox div[data-baseweb="select"] > div {
        background: white !important;
        border: 2px solid #d1d5db !important;
        border-radius: 10px !important;
    }

    .stSelectbox div[data-baseweb="select"] > div:hover {
        border-color: #9ca3af !important;
    }

    /* Dropdown options - make them black */
    [data-popover] {
        background: white !important;
    }

    [data-popover] [role="option"] span {
        color: #000000 !important;
        font-weight: 500 !important;
    }

    [data-popover] [role="option"]:hover {
        background: #f3f4f6 !important;
    }

    /* Selected value in selectbox - make it BLACK and BOLD */
    [data-baseweb="select"] [aria-selected="true"] span {
        color: #000000 !important;
        font-weight: 700 !important;
    }

    [data-baseweb="select"] span[data-default="true"] {
        color: #000000 !important;
    }

    /* Target the displayed selected value */
    .stSelectbox [data-testid="stSelectboxValue"],
    .stSelectbox [data-testid="stSelectboxValue"] span,
    .stSelectbox div[role="combobox"],
    .stSelectbox div[role="combobox"] span {
        color: #000000 !important;
        font-weight: 700 !important;
    }

    /* Force black text everywhere in selectbox */
    .stSelectbox * {
        color: #000000 !important;
    }

    /* Make text visible in input */
    input[type="number"] {
        color: #111827 !important;
    }

    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #2563eb, #1d4ed8) !important;
        border: none !important;
        padding: 14px 32px !important;
        font-size: 1.1rem !important;
        font-weight: 600 !important;
        border-radius: 12px !important;
    }

    .stButton > button:hover {
        background: linear-gradient(135deg, #1d4ed8, #1e40af) !important;
    }

    /* Result boxes */
    .result-positive {
        background: linear-gradient(135deg, #fef2f2, #fee2e2);
        border: 3px solid #fca5a5;
        border-radius: 16px;
        padding: 24px;
        text-align: center;
        margin: 16px 0;
    }

    .result-negative {
        background: linear-gradient(135deg, #f0fdf4, #dcfce7);
        border: 3px solid #86efac;
        border-radius: 16px;
        padding: 24px;
        text-align: center;
        margin: 16px 0;
    }

    .result-positive h2 {
        color: #dc2626;
        font-size: 1.8rem;
        margin-bottom: 8px;
    }

    .result-negative h2 {
        color: #16a34a;
        font-size: 1.8rem;
        margin-bottom: 8px;
    }

    .confidence-badge {
        display: inline-block;
        background: #1f2937;
        color: white;
        padding: 8px 20px;
        border-radius: 20px;
        font-weight: 600;
        font-size: 1rem;
    }

    /* Metric cards */
    .metric-box {
        background: #f9fafb;
        border-radius: 12px;
        padding: 20px;
        text-align: center;
    }

    .metric-box h3 {
        font-size: 0.9rem;
        color: #6b7280;
        font-weight: 500;
        margin-bottom: 8px;
    }

    .metric-box .value {
        font-size: 1.6rem;
        font-weight: 700;
    }

    .metric-box.ckd .value {
        color: #dc2626;
    }

    .metric-box.not-ckd .value {
        color: #16a34a;
    }

    /* Recommendation boxes */
    .recommend-box {
        border-radius: 12px;
        padding: 20px;
        margin-top: 16px;
    }

    .recommend-box.danger {
        background: #fef2f2;
        border-left: 4px solid #dc2626;
    }

    .recommend-box.success {
        background: #f0fdf4;
        border-left: 4px solid #16a34a;
    }

    .recommend-box h4 {
        font-size: 1.1rem;
        font-weight: 600;
        margin-bottom: 8px;
    }

    .recommend-box.danger h4 {
        color: #dc2626;
    }

    .recommend-box.success h4 {
        color: #16a34a;
    }

    .recommend-box p {
        color: #4b5563;
        font-size: 0.95rem;
        line-height: 1.5;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
    <div class="custom-header">
        <h1>🫘 Chronic Kidney Disease Prediction</h1>
        <p>Machine Learning Powered Health Assessment</p>
    </div>
""", unsafe_allow_html=True)

# Blood Test Results
st.markdown('<div class="form-card">', unsafe_allow_html=True)
st.markdown('<p class="section-title">🩸 Blood Test Results</p>', unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)

with c1:
    age  = st.number_input("Age (years)", min_value=0.0, max_value=120.0, value=48.0, help="Patient age")
    sg   = st.number_input("Specific Gravity", min_value=1.0, max_value=1.5, value=1.020, step=0.001, help="Urine specific gravity")
    bgr  = st.number_input("Blood Glucose (mg/dL)", min_value=0.0, value=121.0, help="Random blood sugar")
    sc   = st.number_input("Serum Creatinine (mg/dL)", min_value=0.0, value=1.2, help="Kidney function marker")
    hemo = st.number_input("Hemoglobin (g/dL)", min_value=0.0, value=15.4, help="Red blood cell protein")

with c2:
    bp   = st.number_input("Blood Pressure (mmHg)", min_value=0.0, value=80.0, help="Systolic BP")
    al   = st.number_input("Albumin (0-5)", min_value=0, max_value=5, value=1, help="Urine albumin")
    bu   = st.number_input("Blood Urea (mg/dL)", min_value=0.0, value=36.0, help="Waste product indicator")
    sod  = st.number_input("Sodium (mEq/L)", min_value=0.0, value=140.0, help="Blood sodium level")
    pcv  = st.number_input("Packed Cell Volume (%)", min_value=0.0, value=44.0, help="Red blood cell %")

with c3:
    su   = st.number_input("Sugar (mg/dL)", min_value=0.0, value=0.0, help="Urine sugar level")
    pot  = st.number_input("Potassium (mEq/L)", min_value=0.0, value=4.0, help="Blood potassium")
    wbcc = st.number_input("WBC Count", min_value=0.0, value=7800.0, help="White blood cells")
    rbcc = st.number_input("RBC Count", min_value=0.0, value=5.2, help="Red blood cells")

st.markdown('</div>', unsafe_allow_html=True)

# Clinical Observations
st.markdown('<div class="form-card">', unsafe_allow_html=True)
st.markdown('<p class="section-title">🩺 Clinical Observations</p>', unsafe_allow_html=True)

c4, c5 = st.columns(2)

with c4:
    rbc   = st.selectbox("Red Blood Cells", ["normal", "abnormal"])
    pcc   = st.selectbox("Pus Cell Clumps", ["notpresent", "present"])
    htn   = st.selectbox("Hypertension", ["no", "yes"])
    cad   = st.selectbox("Coronary Artery Disease", ["no", "yes"])
    pe    = st.selectbox("Pedal Edema", ["no", "yes"])

with c5:
    pc    = st.selectbox("Pus Cells", ["normal", "abnormal"])
    ba    = st.selectbox("Bacteria", ["notpresent", "present"])
    dm    = st.selectbox("Diabetes Mellitus", ["no", "yes"])
    appet = st.selectbox("Appetite", ["good", "poor"])
    ane   = st.selectbox("Anemia", ["no", "yes"])

st.markdown('</div>', unsafe_allow_html=True)

# Show selected clinical observations
st.markdown('<div class="form-card">', unsafe_allow_html=True)
st.markdown('<p class="section-title">📋 Selected Clinical Observations</p>', unsafe_allow_html=True)

# Display all selected values in a clear format
clinical_data = {
    "Red Blood Cells": rbc,
    "Pus Cells": pc,
    "Pus Cell Clumps": pcc,
    "Bacteria": ba,
    "Hypertension": htn,
    "Diabetes Mellitus": dm,
    "Coronary Artery Disease": cad,
    "Appetite": appet,
    "Pedal Edema": pe,
    "Anemia": ane
}

# Create columns for display
cols = st.columns(5)
for i, (label, value) in enumerate(clinical_data.items()):
    with cols[i % 5]:
        # Color code the value
        if value in ["abnormal", "present", "yes", "poor"]:
            color = "#dc2626"
            bg = "#fef2f2"
        else:
            color = "#16a34a"
            bg = "#f0fdf4"

        st.markdown(f"""
            <div style="background:{bg}; padding:12px; border-radius:10px; text-align:center; margin-bottom:8px;">
                <p style="color:#6b7280; font-size:0.75rem; margin:0; font-weight:500;">{label}</p>
                <p style="color:{color}; font-size:1rem; margin:4px 0 0 0; font-weight:700;">{value.upper()}</p>
            </div>
        """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Predict Button
st.markdown("<br>", unsafe_allow_html=True)
if st.button("🔍 Analyze & Predict CKD Risk", use_container_width=True, type="primary"):
    payload = {
        "age": age, "bp": bp, "sg": sg, "al": al, "su": su,
        "bgr": bgr, "bu": bu, "sc": sc, "sod": sod, "pot": pot,
        "hemo": hemo, "pcv": pcv, "wbcc": wbcc, "rbcc": rbcc,
        "rbc": rbc, "pc": pc, "pcc": pcc, "ba": ba,
        "htn": htn, "dm": dm, "cad": cad, "appet": appet,
        "pe": pe, "ane": ane
    }

    with st.spinner("🤖 Running ML Analysis..."):
        try:
            res = requests.post(f"{API_URL}/predict", json=payload)
            res.raise_for_status()
            data = res.json()

            is_ckd = data["label"] == "ckd"
            confidence = data["confidence"] * 100
            ckd_pct = data["probabilities"]["ckd"] * 100
            notckd_pct = data["probabilities"]["notckd"] * 100

            st.markdown("<br>", unsafe_allow_html=True)

            # Result Box
            if is_ckd:
                st.markdown(f"""
                    <div class="result-positive">
                        <h2>⚠️ CKD Detected</h2>
                        <span class="confidence-badge">{confidence:.1f}% Confidence</span>
                    </div>
                """, unsafe_allow_html=True)

                st.markdown("""
                    <div class="recommend-box danger">
                        <h4>🏥 Immediate Action Required</h4>
                        <p>High risk of CKD detected. Please consult a nephrologist immediately for comprehensive evaluation and treatment planning.</p>
                    </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                    <div class="result-negative">
                        <h2>✅ No CKD Detected</h2>
                        <span class="confidence-badge">{confidence:.1f}% Confidence</span>
                    </div>
                """, unsafe_allow_html=True)

                st.markdown("""
                    <div class="recommend-box success">
                        <h4>💚 Healthy</h4>
                        <p>Kidney function appears normal. Continue maintaining a healthy lifestyle and regular checkups.</p>
                    </div>
                """, unsafe_allow_html=True)

            # Probability Display
            st.markdown("<br>", unsafe_allow_html=True)
            m1, m2 = st.columns(2)

            with m1:
                st.markdown(f"""
                    <div class="metric-box ckd">
                        <h3>CKD Probability</h3>
                        <div class="value">{ckd_pct:.1f}%</div>
                    </div>
                """, unsafe_allow_html=True)
                st.progress(ckd_pct / 100)

            with m2:
                st.markdown(f"""
                    <div class="metric-box not-ckd">
                        <h3>Non-CKD Probability</h3>
                        <div class="value">{notckd_pct:.1f}%</div>
                    </div>
                """, unsafe_allow_html=True)
                st.progress(notckd_pct / 100)

            # Feature Importance Graph
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown('<div class="form-card">', unsafe_allow_html=True)
            st.markdown('<p class="section-title">📊 Feature Importance</p>', unsafe_allow_html=True)
            st.image("report/feature_importance.png", use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
            st.info("Make sure FastAPI server is running on port 8000")


# Footer
st.markdown("---")
st.markdown("""
    <div style="text-align:center; color:#6b7280; padding:20px; font-size:0.9rem;">
        <p><b>Powered by Random Forest Classifier</b></p>
        <p style="font-size:0.8rem;">For demonstration only. Not a substitute for professional medical advice.</p>
    </div>
""", unsafe_allow_html=True)