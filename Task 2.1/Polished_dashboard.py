import streamlit as st
import pandas as pd
import plotly.express as px

# Sample data
data = {
    'Category': ['A', 'B', 'C', 'D', 'E','F','G'],
    'Value': [25, 30, 15, 20, 10,20,50]
}
df = pd.DataFrame(data)

# Streamlit app
st.title("Interactive Dashboard")

# Show the data table
st.subheader("Data Table")
st.dataframe(df)

# Create a bar chart using Plotly Express
fig = px.bar(df, x='Category', y='Value', title='Bar Chart Example', color='Category')
st.plotly_chart(fig)

# Interactive widget to filter data
selected_category = st.selectbox("Select a Category:", df['Category'])
filtered_df = df[df['Category'] == selected_category]
st.subheader("Filtered Data")
st.dataframe(filtered_df)


#streamlit run polished_dashboard.py