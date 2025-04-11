import streamlit as st

# Define pages as functions
def home():
    st.title("Home")
    st.write("Welcome to our multi-page Streamlit website!")

def about():
    st.title("About")
    st.write("This is a demo app built with Streamlit.")

def contact():
    st.title("Contact")
    st.write("You can contact us at: example@example.com")

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ("Home", "About", "Contact"))

if page == "Home":
    home()
elif page == "About":
    about()
elif page == "Contact":
    contact()