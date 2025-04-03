import streamlit as st
import requests
import pandas as pd
import streamlit as st


data = [
        {"Store #": 440, "State": "New Jersey","Employees": 4, "Closed": True},
        {"Store #": 430, "State": "South Carolina", "Employees": 5, "Closed": False},
        {"Store #": 250, "State": "South Carolina", "Employees": 3, "Closed": True},
        {"Store #": 360, "State": "South Carolina", "Employees": 3, "Closed": True},
        {"Store #": 420, "State": "Georgia", "Employees": 6, "Closed": True},
        {"Store #": 220, "State": "West Virginia", "Employees": 3, "Closed": True},
        {"Store #": 5670, "State": "West Virginia", "Employees": 6, "Closed": True},
        {"Store #": 489, "State": "Iowa", "Employees": 4, "Closed": True},
        {"Store #": 440, "State": "North Carolina", "Employees": 6, "Closed": True},
    ]
df = pd.DataFrame(data)

if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = True


# Fedex Data (API)
st.title("Fedex Store Management")

option1 = st.selectbox(
    "Location",
    (df["State"]),
)
option2 = st.selectbox(
    "Store #",
    (df["Store #"]),
    disabled=True
)

st.divider()
st.write("You selected store:", option2, "in", option1)

df = df[df['State'] == option1]
st.write(df)



st.divider()




# Datatable with SQL server
st.title("Test Api Call")
st.write("Need a SQL Database to connect, using star wars api for now")

try:
    data = requests.get("https://swapi.dev/api/planets/").json()
except:
    print("no data")

st.dataframe(
    data['results'],
    selection_mode="multi-row",
    column_config={
        "name":"Planet",
        "climate":"Weather"
    },
)
