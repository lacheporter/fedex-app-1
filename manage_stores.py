import streamlit as st
import requests
import pandas as pd
import streamlit as st

#import data
data = pd.read_json('data.json')
# Create a dataframe...
df = pd.DataFrame(data)

#Create Title, Columns, Select boxes, drop duplicates...
st.title("Fedex Store Management")
st.subheader("Manage your store data.")
st.write("Select your location and store to start editing!")
col1, col2 = st.columns([2, 1])
states = df["State"].drop_duplicates()
with col1:
    option1 = st.selectbox("Location", (states), key=1)

# Create select box of Stores based on State choice...
stores = df[df["State"] == option1]
with col2:
    option2 = st.selectbox("Store #", stores["Store"], key=2)

st.write("You selected Store:", option2, "in", option1)
st.divider()

st.write("Store Information:")
# Print and display filtered Dataframe
df = df[(df['State'] == option1) & (df['Store'] == option2)]
st.dataframe(df, column_config={"Employees": None, "Inventory": None})

#create editable dataframe from inventory
st.write("Inventory Information:")
inventoryItems =[]
for items in df["Inventory"]:
    inventoryItems.append(items)
st.data_editor(inventoryItems)

st.write("Employee Information:")
EmployeeItems =[]
for items in df["Employees"]:
    EmployeeItems.append(items)
st.data_editor(items)
st.divider()

st.title("Import Store Data")
st.write("Import CSV of your existing store information.")

st.divider()

#API request testing...
st.title("Explore Store")
st.write("Need a SQL Database to connect, using star wars api for now")
try:
    data = requests.get("https://swapi.dev/api/planets/").json()
except:
    print("no data")
st.dataframe(
    data['results'],
    selection_mode="multi-row",
    column_config={
        "name": "Planet",
        "climate": "Weather"
    },
)
