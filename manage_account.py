import streamlit as st

st.title("Account Management")
st.write("Welcome! Nothing to see here")

import streamlit as st

if not st.experimental_user.is_logged_in:
    if st.button("Log in"):
        st.login()
else:
    if st.button("Log out"):
        st.logout()
    st.write(f"Hello, {st.experimental_user.name}!")