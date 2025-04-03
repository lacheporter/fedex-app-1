import streamlit as st
import pandas as pd

import streamlit as st

pages = {
    "Your account": [
        st.Page("manage_account.py", title="My Account"),
        st.Page("manage_stores.py", title="My Stores")
    ],
    "Resources": [
        st.Page("learn.py", title="Tutorials"),
    ],
}

pg = st.navigation(pages)
pg.run()

