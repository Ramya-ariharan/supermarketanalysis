# streamlit_app.py
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("Superstore.csv", encoding='ISO-8859-1')
df['Order Date'] = pd.to_datetime(df['Order Date'])

st.title("Superstore Dashboard")

category = st.selectbox("Choose Category", df['Category'].unique())
filtered = df[df['Category'] == category]

st.write(filtered.groupby('Sub-Category')['Sales'].sum())

fig, ax = plt.subplots()
sns.boxplot(x='Segment', y='Profit', data=filtered, ax=ax)
st.pyplot(fig)


# # test_streamlit.py
# import streamlit as st

# st.title("Hello, Ramya 👋")
# st.write("Your Streamlit app is working!")
