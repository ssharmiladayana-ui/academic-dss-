import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image

st.set_page_config(page_title="GONZAGA DSS", page_icon="🎓", layout="wide")

# --- CSS ---
st.markdown("""
<style>
.stApp { background: linear-gradient(135deg, #f4ecf7, #d2b4de); }
.login-bg { background: linear-gradient(135deg, #5b2c6f, #8e44ad); padding: 40px 0; }
.login-card {
    background: white;
    padding: 30px;
    border-radius: 15px;
    box-shadow: 0 8px 30px rgba(0,0,0,0.2);
}
</style>
""", unsafe_allow_html=True)

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# --- LOGIN PAGE ---
if not st.session_state.logged_in:
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        try:
            st.image("logo.png")
        except:
            st.markdown("<h1 style='text-align:center; color:#4a235a;'>🎓 GONZAGA COLLEGE</h1>", unsafe_allow_html=True)
        
        st.markdown('<div class="login-card">', unsafe_allow_html=True)
        st.markdown("<h3 style='text-align:center;color:#4a235a;'>GONZAGA COLLEGE OF ARTS AND SCIENCE FOR WOMEN</h3><p style='text-align:center;'>Academic Decision Support System</p>", unsafe_allow_html=True)
        user = st.text_input("Username")
        pwd = st.text_input("Password", type="password")
        if st.button("LOGIN", use_container_width=True, type="primary"):
            if user == "admin" and pwd == "admin123":
                st.session_state.logged_in = True
                st.rerun()
            else:
                st.error("Invalid login! Use admin / admin123")
        st.markdown('</div>', unsafe_allow_html=True)
    st.stop()

# --- AFTER LOGIN - MAIN PROJECT ---
with st.sidebar:
    try:
        st.image("logo.png", width=200)
    except:
        pass
    st.markdown("### 🎓 GONZAGA COLLEGE")
    st.markdown("Academic DSS")
    st.divider()
    menu = st.selectbox("Menu", ["Dashboard", "Student Analysis", "Performance Prediction"])
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()

st.title("📊 Academic Decision Support System")
st.subheader("GONZAGA COLLEGE OF ARTS AND SCIENCE FOR WOMEN")

if menu == "Dashboard":
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Students", "350", "12")
    col2.metric("Pass %", "89%", "5%")
    col3.metric("Avg CGPA", "7.8", "0.3")
    col4.metric("Placements", "120", "15")
    
    st.divider()
    # Sample data
    data = pd.DataFrame({
        "Department": ["CS", "BCA", "Maths", "Commerce", "English"],
        "Pass Percentage": [92, 88, 85, 90, 87]
    })
    fig = px.bar(data, x="Department", y="Pass Percentage", color="Department", title="Department Wise Performance")
    st.plotly_chart(fig, use_container_width=True)

elif menu == "Student Analysis":
    st.write("Upload Student Data CSV or view sample analysis")
    uploaded = st.file_uploader("Upload CSV", type=["csv"])
    if uploaded:
        df = pd.read_csv(uploaded)
        st.dataframe(df)
    else:
        sample_df = pd.DataFrame({
            "Name": ["Priya", "Anu", "Divya", "Lakshmi", "Kavya"],
            "Dept": ["CS", "CS", "BCA", "Commerce", "Maths"],
            "CGPA": [8.5, 7.2, 9.0, 8.0, 7.8],
            "Attendance": [95, 88, 92, 85, 90]
        })
        st.dataframe(sample_df)
        fig2 = px.scatter(sample_df, x="Attendance", y="CGPA", color="Dept", size="CGPA", hover_name="Name", title="Attendance vs CGPA")
        st.plotly_chart(fig2)

elif menu == "Performance Prediction":
    st.info("AI based prediction for at-risk students")
    st.write("Enter student details:")
    cgpa = st.slider("Current CGPA", 0.0, 10.0, 7.5)
    att = st.slider("Attendance %", 0, 100, 85)
    if st.button("Predict"):
        if cgpa < 6 or att < 75:
            st.error("⚠️ At Risk - Need Counselling")
        else:
            st.success("✅ Good Performance - On Track")
