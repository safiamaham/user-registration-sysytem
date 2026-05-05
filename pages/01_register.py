import streamlit as st
import re #register expressions
from utils import(
    validate_email,
    validate_phone, 
    validate_password,
    validate_name,
    validate_login,
    validate_user_id,
    save_user

)

st.set_page_config(
    page_title = "User  Registeration ",
    layout="centered"
)
st.title("User Registration Form")
if 'form_submitted' not in st.session_state:
    st.session_state.form_submitted = False

with st.form("registration_form",clear_on_submit=False):
    col1, col2 = st.columns(2)
    with col1:
        user_id = st.text_input("User ID", placeholder="eg:Rafay123", help="4-20 Characters(letters, numbers and underscore)")
        full_name = st.text_input("Full Name", placeholder="eg: Rafay Ahmed", help="2- Characters(letters, spaces and hyphens)")
        email = st.text_input("Email", placeholder="eg: rafay@example.com", help="Must Be Valid Email Address")
    with col2:
        phone = st.text_input("Phone Number", placeholder="eg: +923362327095", help="Pakistan format only")
        password = st.text_input("Password", placeholder="eg: Enter Your Password", help="8-20 Characters with uppercase, lowercase, numbers and special characters")
        confirm_password = st.text_input("Confirm Password", placeholder="eg: Re-enter Your Password")
    submit_button = st.form_submit_button("Register Now", type="primary")
