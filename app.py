import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Academic DSS", layout="centered")
st.title("🎓 Smart Academic Decision Support System")
st.write("Naan Mudhalvan Project - Dropout Risk Predictor")

st.header("Student Details Enter Pannu")

col1, col2 = st.columns(2)
with col1:
    tenth = st.number_input("10th Marks %", 35, 100, 85)
    sem1 = st.slider("Sem 1 GPA", 0.0, 10.0, 7.5)
    attendance = st.slider("Attendance %", 0, 100, 75)
with col2:
    twelfth = st.number_input("12th Marks %", 35, 100, 80)
    sem2 = st.slider("Sem 2 GPA", 0.0, 10.0, 7.0)
    backlogs = st.number_input("Backlogs", 0, 10, 0)

if st.button("Predict Risk"):
    risk_score = 0
    if attendance < 75: risk_score += 40
    if backlogs > 1: risk_score += 30
    if sem1 < 6.0 or sem2 < 6.0: risk_score += 30

    if risk_score >= 50:
        st.error(f"🔴 HIGH RISK - {risk_score}% - Counselor kitta pesanum!")
        st.write("Suggestion: Naan Mudhalvan courses eduthuko, attendance improve pannu.")
    elif risk_score >= 30:
        st.warning(f"🟡 MEDIUM RISK - {risk_score}% - Careful ah iru.")
    else:
        st.success(f"🟢 LOW RISK - {risk_score}% - Nalla poittu irukka!")

st.divider()
st.header("HOD Dashboard (Demo)")
chart_data = pd.DataFrame(np.random.randint(60, 100, size=(10, 1)), columns=['Attendance'])
st.bar_chart(chart_data)
st.caption("Intha chart HOD ku students overall performance paarka")
import streamlit as st

# --- LOGIN PART ---
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.title("🔐 Login Pannu")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        if username == "admin" and password == "admin123":
            st.session_state.logged_in = True
            st.success("Login Success! Loading...")
            st.rerun()
        else:
            st.error("Username / Password thappu da!")
    st.stop() # Login pannama ulla vara mudiyathu
# --- LOGIN MUDINJIDUCHU ---

