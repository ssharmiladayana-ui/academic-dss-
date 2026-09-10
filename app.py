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
            elif menu == "Performance Prediction":
    st.header("📊 Student Mark Prediction")

    # Student name select panna
    student_name = st.selectbox("Student Name ah select pannu", 
                                ["Sharmila", "Priya", "Keerthi", "Divya"])

    # Input edukkura edam
    attendance = st.slider("Attendance %", 0, 100, 75)
    internal_mark = st.slider("Internal Mark (out of 50)", 0, 50, 35)
    study_hours = st.slider("Daily Study Hours", 0, 10, 3)

    if st.button("Predict Mark"):
        # Simple prediction formula - ML model ku pathila
        predicted_mark = (attendance * 0.3) + (internal_mark * 1.2) + (study_hours * 5)
        
        if predicted_mark > 100:
            predicted_mark = 95

        st.success(f"✅ {student_name} oda Predicted Mark: {predicted_mark:.1f} / 100")
        
        if predicted_mark >= 60:
            st.balloons()
            st.write("🎉 Pass aayiduvanga!")
        else:
            st.warning("⚠️ Konjam extra coaching venum")
            elif menu == "Performance Prediction":
    st.header("🎯 350 Students Prediction")
    import pandas as pd
    import random

    try:
        # WPS Excel file ah padikka
        df = pd.read_excel("students.xlsx") # un file name.xlsx nu iruntha
        st.success(f"✅ {len(df)} students load aayiduchu! WPS file than!")

        # Random ah eduthu kaamikura
        if st.button("🎲 Random Student ahh Predict pannu", use_container_width=True):
            row = df.sample(1).iloc[0]
            name = str(row.iloc[0]) # first column la name irukkum

            st.success(f"**Student: {name}**")
            st.write(row) # full details kaamikura

            # Mark predict
            pred = random.randint(55, 98)
            st.metric("Predicted Final Mark", f"{pred}/100")
            st.progress(pred)

        st.divider()
        # Search pannura option
        student_list = df.iloc[:,0].astype(str).tolist() # first column la ellam name
        selected = st.selectbox(f"350 per la oruthara thedu ({len(student_list)} students)", student_list)

        if selected:
            student_data = df[df.iloc[:,0].astype(str) == selected].iloc[0]
            st.write("**Avanga Details:**")
            st.dataframe(student_data)

    except Exception as e:
        st.error(f"File kedaikala da: {e}")
        st.info("students.xlsx file ah GitHub la upload panniya nu check pannu")
