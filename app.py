import streamlit as st
from PIL import Image

st.set_page_config(page_title="GONZAGA DSS", page_icon="🎓", layout="centered")

st.markdown("""
<style>
.stApp { background: linear-gradient(135deg, #5b2c6f, #8e44ad, #d2b4de); }
.login-card {
    background: rgba(255,255,255,0.92);
    padding: 35px;
    border-radius: 15px;
    box-shadow: 0 8px 30px rgba(0,0,0,0.2);
}
</style>
""", unsafe_allow_html=True)

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    with st.container():
        col1, col2, col3 = st.columns([1,3,1])
        with col2:
            try:
                st.image("logo.png", use_container_width=True)
            except:
                st.markdown("<h1 style='text-align:center;color:white;'>GONZAGA COLLEGE</h1>", unsafe_allow_html=True)
            
            st.markdown('<div class="login-card">', unsafe_allow_html=True)
            st.markdown("<h2 style='text-align:center;color:#4a235a;'>Welcome Back</h2><p style='text-align:center;'>Sign in to Academic DSS</p>", unsafe_allow_html=True)
            user = st.text_input("Username")
            pwd = st.text_input("Password", type="password")
            if st.button("LOGIN", use_container_width=True, type="primary"):
                if user == "admin" and pwd == "admin123":
                    st.session_state.logged_in = True
                    st.rerun()
                else:
                    st.error("Invalid Username/Password")
            st.markdown("<p style='text-align:center;font-size:12px;'>© 2024 GONZAGA COLLEGE OF ARTS AND SCIENCE FOR WOMEN</p>", unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
    st.stop()

with st.sidebar:
    try:
        st.image("logo.png")
    except:
        pass
    st.write("**GONZAGA COLLEGE**")
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()


