import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image
import random

st.set_page_config(page_title="GONZAGA DSS", page_icon="🎓", layout="wide")

# --- CSS ---
st.markdown("""
<style>
.stApp { background: linear-gradient(135deg, #f4ecf7, #d2b4de); }
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

# --- AFTER LOGIN ---
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
    col1.metric("Total Students", "500", "150")
    col2.metric("Pass %", "89%", "5%")
    col3.metric("Avg CGPA", "7.8", "0.3")
    col4.metric("At-Risk", "45", "-5")
    st.divider()
    data = pd.DataFrame({
        "Department": ["CS", "BCA", "Maths", "Commerce", "English"],
        "Pass Percentage": [92, 88, 85, 90, 87]
    })
    fig = px.bar(data, x="Department", y="Pass Percentage", color="Department", title="Department Wise Performance")
    st.plotly_chart(fig, use_container_width=True)

elif menu == "Student Analysis":
    st.header("📈 Student Analysis")
    try:
        df_main = pd.read_csv("students.csv")
        st.dataframe(df_main.head(100), use_container_width=True)
        fig2 = px.scatter(df_main, x="attendance", y="sem2_gpa", color="dropout_risk", hover_name="student_id", title="Attendance vs Sem2 GPA (Red=At Risk)")
        st.plotly_chart(fig2, use_container_width=True)
    except:
        st.info("Upload CSV in Student Analysis")
        uploaded = st.file_uploader("Upload CSV", type=["csv"])
        if uploaded:
            df = pd.read_csv(uploaded)
            st.dataframe(df)

elif menu == "Performance Prediction":
    st.header("🎯 Performance Prediction - Student ID Based")
    try:
        df = pd.read_csv("students.csv")
        st.success(f"✅ {len(df)} Students Ready! (STU001 - STU{len(df)})")

        tab1, tab2 = st.tabs(["🎲 Random Student", "🔍 Search by Student ID"])

        with tab1:
            if st.button("Random Student ID eduthu Predict pannu", use_container_width=True, type="primary"):
                row = df.sample(1).iloc[0]

                st.success(f"**Student ID: {row['student_id']}**")

                c1,c2,c3,c4 = st.columns(4)
                c1.metric("10th Marks", row['10th_marks'])
                c2.metric("12th Marks", row['12th_marks'])
                c3.metric("Sem1 GPA", row['sem1_gpa'])
                c4.metric("Sem2 GPA", row['sem2_gpa'])

                c5,c6,c7 = st.columns(3)
                c5.metric("Attendance", f"{row['attendance']}%")
                c6.metric("Backlogs", row['backlogs'])
                c7.metric("Risk", "YES 🔴" if row['dropout_risk']==1 else "NO 🟢")

                sem_avg = (row['sem1_gpa'] + row['sem2_gpa'])/2
                pred = (sem_avg * 0.7) + (row['attendance']/100 * 2) - (row['backlogs']*0.5)
                if pred > 10: pred = 9.8
                if pred < 0: pred = 4.0

                st.divider()
                st.metric("🔮 Predicted Final GPA", f"{pred:.2f} / 10.0")
                st.progress(int((pred/10)*100))

                if row['dropout_risk'] == 1 or pred < 6:
                    st.error(f"⚠️ {row['student_id']} - At-Risk! Counselling venum")
                else:
                    st.balloons()
                    st.success("✅ Good Performance - On Track")

        with tab2:
            student_ids = df['student_id'].astype(str).tolist()
            selected = st.selectbox(f"Student ID select pannu ({len(student_ids)} IDs)", student_ids)

            if selected:
                found = df[df['student_id'].astype(str) == selected].iloc[0]
                st.write(f"**{selected} Details:**")
                st.dataframe(found.to_frame().T, use_container_width=True)

                sem_avg = (found['sem1_gpa'] + found['sem2_gpa'])/2
                pred = (sem_avg * 0.7) + (found['attendance']/100 * 2) - (found['backlogs']*0.5)
                if pred > 10: pred = 9.8

                st.metric(f"🔮 {selected} Predicted GPA", f"{pred:.2f} / 10")

                if found['dropout_risk'] == 1:
                    st.error("⚠️ Dropout Risk irukku")
                else:
                    st.success("✅ Safe")

    except FileNotFoundError:
        st.error("❌ students.csv file GitHub la illa da!")
    except Exception as e:
        st.error(f"Error: {e}")
