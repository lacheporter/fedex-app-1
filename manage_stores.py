import streamlit as st
import requests
import pandas as pd
import streamlit as st

data = [
        {"Store": 440, "State": "New Jersey","Employees": 4, "Closed": True},
        {"Store": 760, "State": "New Jersey","Employees": 4, "Closed": True},
        {"Store": 430, "State": "South Carolina", "Employees": 5, "Closed": False},
        {"Store": 250, "State": "South Carolina", "Employees": 3, "Closed": True},
        {"Store": 360, "State": "South Carolina", "Employees": 3, "Closed": True},
        {"Store": 420, "State": "Georgia", "Employees": 6, "Closed": True},
        {"Store": 220, "State": "West Virginia", "Employees": 3, "Closed": True},
        {"Store": 567, "State": "West Virginia", "Employees": 6, "Closed": True},
        {"Store": 489, "State": "Iowa", "Employees": 4, "Closed": True},
        {"Store": 440, "State": "North Carolina", "Employees": 6, "Closed": True},
    ]

st.title("Fedex Store Management")

#Create a dataframe...
df = pd.DataFrame(data)

col1, col2 = st.columns([2, 1])
#Create Select box of States, drop duplicates...
states = df["State"].drop_duplicates()
with col1:
    option1 = st.selectbox("Location",(states),key=1)

#Create select box of Stores based on State choice...
stores = df[df["State"] == option1]
with col2:
    option2 = st.selectbox("Store #", stores["Store"], key=2)


st.divider()

#Print and display filtered Dataframe
df = df[(df['State']==option1) & (df['Store']==option2)]
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
