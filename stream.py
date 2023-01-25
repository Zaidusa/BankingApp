import streamlit as st

from BankingData import Banking
from dbconnect import DBConnection


st.title("The Customer Banking online Application")
menu = ["Home", "Login", "SignUp"]
choice = st.sidebar.selectbox("Menu", menu)
if choice == "Home":
    st.subheader("You are in login Page, enter valid credentials to observe your account data")
elif choice == "Login":
    st.subheader("user data")


db=DBConnection()

username = st.sidebar.text_input("User Name")
password = st.sidebar.text_input("Password")
print(f"data entered is {username},{password}")
data=db.login_user(username,password)
authenticated_users=db.view_all_users()
print ("this is the data", data)
if st.sidebar.checkbox("Login"):
    if (data):
        st.success (f"authenticated user, {username}")
        Banking.Bank()

    else:
        st.fail(f"unauthenticated user, {username}")


