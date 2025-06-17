import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv("Superstore.csv", encoding='ISO-8859-1')

# Convert to datetime
df['Order Date'] = pd.to_datetime(df['Order Date'])

st.set_page_config(page_title="📦 Superstore Dashboard", layout="wide")

st.title("📦 Superstore Sales Dashboard")

# Optional filter
with st.sidebar:
    st.header("🔍 Filters")
    region = st.selectbox("Choose Region", ["All"] + list(df['Region'].unique()))
    category = st.selectbox("Choose Category", ["All"] + list(df['Category'].unique()))

# Filter logic
filtered = df.copy()
if region != "All":
    filtered = filtered[filtered['Region'] == region]
if category != "All":
    filtered = filtered[filtered['Category'] == category]

# Plot 1: Profit by Sub-Category
st.subheader("💰 Profit by Sub-Category")
fig1, ax1 = plt.subplots()
sns.barplot(x='Profit', y='Sub-Category', 
            data=filtered.sort_values('Profit', ascending=False),
              ax=ax1, palette="coolwarm")
st.pyplot(fig1)

# Plot 2: Discount vs Profit
st.subheader("🎯 Discount vs Profit")
fig2, ax2 = plt.subplots()
sns.scatterplot(data=filtered,
                 x='Discount',
                   y='Profit', 
                   hue='Segment', ax=ax2)
st.pyplot(fig2)

# Plot 3: Monthly Sales
st.subheader("📆 Monthly Sales Trend")
filtered['Month'] = filtered['Order Date'].dt.to_period("M")
monthly = filtered.groupby('Month')['Sales'].sum()

fig3, ax3 = plt.subplots()
monthly.plot(kind='line', marker='o', color='purple', ax=ax3)
ax3.set_ylabel("Sales")
st.pyplot(fig3)




# Plot 1: Profit by Sub-Category (clean version)
st.subheader("💰 Profit by Sub-Category (Clean View)")
fig1, ax1 = plt.subplots(figsize=(10, 6))

# Sort data
sorted_profit = filtered.groupby('Sub-Category')['Profit'].sum().sort_values()

# Plot without error bars and clean style
sns.barplot(x=sorted_profit.values, y=sorted_profit.index, palette='coolwarm', ax=ax1, errorbar=None)

# Add labels
ax1.set_xlabel("Total Profit")
ax1.set_ylabel("Sub-Category")
ax1.set_title("Profit by Sub-Category")
st.pyplot(fig1)
