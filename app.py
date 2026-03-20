import streamlit as st
import pickle
import numpy as np
import random
import string

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Axis Bank – Home Loan Portal",
    page_icon="🏦",
    layout="wide"
)

# ── Custom CSS (Shared) ──────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

/* ── Navbar ── */
.navbar {
    background: linear-gradient(90deg, #97144D, #c0185f);
    padding: 0.8rem 2rem;
    border-radius: 0 0 16px 16px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 0;
    box-shadow: 0 4px 24px rgba(151,20,77,0.35);
}
.nav-brand { display: flex; align-items: center; gap: 12px; }
.nav-logo { font-size: 1.6rem; font-weight: 800; color: white; letter-spacing: -0.5px; }
.nav-logo span { color: #ffd700; }
.nav-tagline { color: rgba(255,255,255,0.7); font-size: 0.75rem; letter-spacing: 0.08em; }

/* ── Hero ── */
.hero-banner {
    background: linear-gradient(135deg, #97144D 0%, #c0185f 45%, #ff6b9d 100%);
    border-radius: 16px; padding: 3rem 2.5rem; margin: 1.2rem 0;
    position: relative; overflow: hidden;
}
.hero-title { font-size: 2.2rem; font-weight: 800; color: white; margin-bottom: 0.4rem; }
.hero-sub { font-size: 1rem; color: rgba(255,255,255,0.8); max-width: 520px; line-height: 1.6; }

/* ── Tabs Styling ── */
.stTabs [data-baseweb="tab-list"] {
    gap: 10px;
}
.stTabs [data-baseweb="tab"] {
    height: 50px;
    white-space: pre-wrap;
    background-color: rgba(151, 20, 77, 0.05);
    border-radius: 10px 10px 0 0;
    gap: 1px;
    padding: 10px 20px;
    font-weight: 600;
}
.stTabs [aria-selected="true"] {
    background-color: #97144D !important;
    color: white !important;
}

/* ── Cards & Sections ── */
.section-head {
    font-size: 1.25rem; font-weight: 700; color: #97144D;
    padding-bottom: 0.5rem; border-bottom: 2px solid #97144D;
    margin: 1.5rem 0 1rem 0;
}
.ad-card {
    background: white; border: 1px solid #eee; border-radius: 12px;
    padding: 1.5rem; margin-bottom: 1.2rem; transition: transform 0.2s;
    box-shadow: 0 4px 12px rgba(0,0,0,0.03);
}
.ad-card:hover { transform: translateY(-3px); box-shadow: 0 8px 24px rgba(0,0,0,0.06); }
.ad-title { font-size: 1.1rem; font-weight: 700; color: #97144D; margin-bottom: 8px; }

/* ── Tags ── */
.tag-row { display: flex; flex-wrap: wrap; gap: 8px; margin: 0.5rem 0; }
.tag { padding: 4px 12px; border-radius: 20px; font-size: 0.78rem; font-weight: 600; }
.tag-g { background:#dcfce7; color:#166534; border:1px solid #86efac; }
.tag-b { background:#dbeafe; color:#1e40af; border:1px solid #93c5fd; }

/* ── Result display ── */
.result-box { border-radius: 16px; padding: 2rem; text-align: center; margin-top: 1rem; }
.approved { background: #f0fdf4; border: 1.5px solid #4ade80; }
.rejected { background: #fff1f2; border: 1.5px solid #f87171; }

.footer {
    background: #1a1a2e; color: rgba(255,255,255,0.5);
    text-align: center; padding: 1.5rem; border-radius: 12px;
    font-size: 0.78rem; margin-top: 3rem;
}
</style>
""", unsafe_allow_html=True)

# ── Shared Navbar ─────────────────────────────────────────────────────────────
st.markdown("""
<div class="navbar">
  <div class="nav-brand">
    <div>
      <div class="nav-logo">AXIS <span>BANK</span></div>
      <div class="nav-tagline">BADHTE CHALEIN</div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# ── Main Tabs ─────────────────────────────────────────────────────────────────
tab_home, tab_predict = st.tabs(["🏠 Welcome to Axis", "🔍 Check Eligibility"])

# ── TAB 1: HOME PAGE (Advertisements) ─────────────────────────────────────────
with tab_home:
    st.markdown("""
    <div class="hero-banner">
      <div class="hero-title">Your Dream Home is Closer Than You Think</div>
      <div class="hero-sub">
        Explore a wide range of Axis Bank Home Loans tailored to your needs. 
        Low interest rates, flexible tenures, and happy memories.
      </div>
    </div>
    """, unsafe_allow_html=True)

    col_ad1, col_ad2 = st.columns(2)
    with col_ad1:
        st.markdown("""
        <div class="ad-card">
          <div class="ad-title">🌟 Asha Home Loans</div>
          <p style="color:#666; font-size:0.9rem;">Special loans for first-time home buyers with combined family income starting at ₹15,000.</p>
          <div class="tag-row"><span class="tag tag-g">Min. Income ₹15k</span><span class="tag tag-b">Zero Processing Fee</span></div>
        </div>
        <div class="ad-card">
          <div class="ad-title">🏢 Commercial Property Loans</div>
          <p style="color:#666; font-size:0.9rem;">Empower your business with easy loans for offices, shops, and clinics.</p>
          <div class="tag-row"><span class="tag tag-b">Up to ₹5 Cr</span><span class="tag tag-g">Quick Disbursal</span></div>
        </div>
        """, unsafe_allow_html=True)
    with col_ad2:
        st.markdown("""
        <div class="ad-card">
          <div class="ad-title">🔄 Balance Transfer & Top-up</div>
          <p style="color:#666; font-size:0.9rem;">Switch your existing home loan to Axis Bank and get lower EMIs plus extra funds.</p>
          <div class="tag-row"><span class="tag tag-g">Save up to 1% ROI</span><span class="tag tag-b">Instant Approval</span></div>
        </div>
        <div class="ad-card">
          <div class="ad-title">🌍 NRI Home Loans</div>
          <p style="color:#666; font-size:0.9rem;">Buy your home in India while working abroad with our seamless digital process.</p>
          <div class="tag-row"><span class="tag tag-b">Remote KYC</span><span class="tag tag-g">Dedicated RM</span></div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="section-head">🔥 Current Festive Offers</div>', unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    c1.metric("Home Loan Rate", "8.75%*", "-0.25% Drop")
    c2.metric("Processing Fee", "₹0*", "100% Waiver")
    c3.metric("Max Tenure", "30 Yrs", "Flexible")

    st.info("💡 Tip: Use the 'Check Eligibility' tab to see if you qualify for these offers instantly!")

# ── TAB 2: PREDICTION (Check Eligibility) ────────────────────────────────────
with tab_predict:
    st.markdown('<div class="section-head">📋 Instant Eligibility Check</div>', unsafe_allow_html=True)
    
    # Load artifacts
    @st.cache_resource
    def load_artifacts():
        with open("model.pkl", "rb") as f: model = pickle.load(f)
        with open("scaler.pkl", "rb") as f: scaler = pickle.load(f)
        with open("encoders.pkl", "rb") as f: encoders = pickle.load(f)
        return model, scaler, encoders

    model, scaler, encoders = load_artifacts()

    # Business Rules Layer
    def check_business_rules(app_income, coapp_income, loan_amt, loan_term, credit_hist):
        total_income = app_income + coapp_income
        MIN_INCOME = 25000
        MAX_INCOME_MULTIPLE = 90
        MAX_FOIR = 0.60
        
        if total_income == 0:
            return False, "No income declared", "Verifiable income source is mandatory."
        if total_income < MIN_INCOME:
            return False, f"Income too low (₹{total_income:,.0f}/mo)", f"Combined monthly income must be at least ₹{MIN_INCOME:,.0f}."
        if credit_hist == 0:
            return False, "Poor credit history (CIBIL < 650)", "A good credit score (≥ 650) is mandatory."
        if loan_amt > MAX_INCOME_MULTIPLE * total_income:
            return False, f"Loan too high vs income", f"Axis Bank allows max {MAX_INCOME_MULTIPLE}× monthly income."
        if loan_term > 0 and (loan_amt / loan_term) / total_income > MAX_FOIR:
            return False, "EMI burden too high", "Estimated EMI exceeds 60% of your income."
        return True, "", ""

    with st.form("loan_form"):
        applicant_name = st.text_input("📝 Full Legal Name", placeholder="Rahul Sharma")
        
        c1, c2, c3 = st.columns(3)
        with c1: gender = st.selectbox("Gender", options=list(encoders["Gender"].classes_))
        with c2: married = st.selectbox("Marital Status", options=list(encoders["Married"].classes_))
        with c3: dependents = st.selectbox("Dependents", options=list(encoders["Dependents"].classes_))

        c4, c5 = st.columns(2)
        with c4: education = st.selectbox("Education", options=list(encoders["Education"].classes_))
        with c5: self_employed = st.selectbox("Self-Employed", options=list(encoders["Self_Employed"].classes_))

        st.markdown("---")
        c6, c7 = st.columns(2)
        with c6:
            applicant_income = st.number_input("Monthly Income (₹)", min_value=0, value=350000)
            loan_amount = st.number_input("Loan Amount (₹)", min_value=0, value=10000000)
        with c7:
            coapplicant_income = st.number_input("Co-applicant Income (₹)", min_value=0, value=0)
            loan_term = st.number_input("Loan Term (months)", min_value=12, value=360)

        c8, c9 = st.columns(2)
        with c8: credit_history = st.selectbox("Credit History", options=[1, 0], format_func=lambda x: "✅ Good" if x == 1 else "❌ Poor")
        with c9: area = st.selectbox("Property Location", options=list(encoders["Area"].classes_))

        submitted = st.form_submit_button("🚀 Check Eligibility Now")

    if submitted:
        ref = "AXS" + "".join(random.choices(string.digits, k=8))
        passed, reason, tip = check_business_rules(applicant_income, coapplicant_income, loan_amount, loan_term, credit_history)

        if not passed:
            st.markdown(f"""<div class="result-box rejected"><h3>🚫 Application Rejected</h3><p><b>Reason:</b> {reason}</p><p>{tip}</p></div>""", unsafe_allow_html=True)
        else:
            # ML Logic
            g_enc = encoders["Gender"].transform([gender])[0]
            m_enc = encoders["Married"].transform([married])[0]
            d_enc = encoders["Dependents"].transform([dependents])[0]
            e_enc = encoders["Education"].transform([education])[0]
            s_enc = encoders["Self_Employed"].transform([self_employed])[0]
            a_enc = encoders["Area"].transform([area])[0]
            
            feat = np.array([[g_enc, m_enc, d_enc, e_enc, s_enc, applicant_income, coapplicant_income, loan_amount, loan_term, credit_history, a_enc]])
            feat_scaled = scaler.transform(feat)
            pred = model.predict(feat_scaled)[0]
            conf = max(model.predict_proba(feat_scaled)[0]) * 100

            if pred == "Y":
                st.markdown(f"""<div class="result-box approved"><h3>🎉 Pre-Approved!</h3><p>Congratulations {applicant_name if applicant_name else "User"}, you are eligible for an Axis Bank loan.</p><p>Ref No: {ref} | Confidence: {conf:.1f}%</p></div>""", unsafe_allow_html=True)
                st.download_button("📂 Download Official Report", f"Axis Bank Loan Report\nName: {applicant_name}\nStatus: Approved\nRef: {ref}", file_name=f"Axis_Report_{ref}.txt")
            else:
                st.markdown(f"""<div class="result-box rejected"><h3>⚠️ Not Eligible</h3><p>Based on our AI model, we cannot approve this loan right now.</p><p>Ref No: {ref} | Confidence: {conf:.1f}%</p></div>""", unsafe_allow_html=True)

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="footer">
  <strong>AXIS BANK LIMITED</strong> &nbsp;|&nbsp; CIN: L65110GJ1993PLC020769<br><br>
  © 2025 Axis Bank Limited. All rights reserved.
</div>
""", unsafe_allow_html=True)
