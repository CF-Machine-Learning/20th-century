import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go




# Configure the page settings
st.set_page_config(
    page_title="Bike Trip Counts and Temperatures Dashboard",
    layout="wide",
    initial_sidebar_state="auto"
)

# Add a title and descriptive text
st.title("Bike Trip Counts and Temperatures Dashboard")
st.markdown("This dashboard displays the bike trip counts and average temperatures for different start stations and for most top 10 most popular station")

top_10_stations = pd.read_csv("Top_10_stations.csv")
Dual_trip_temp = pd.read_csv("Dual_Biketrip_temp.csv")

# Extract month from the 'Date' column
Dual_trip_temp['started_at']=pd.to_datetime(Dual_trip_temp['started_at']).dt.date

# Initialize an empty list to store the selected records
selected_records = []

# Group the data by month
grouped_data = Dual_trip_temp.groupby('started_at')

# Take 5 records from each group
for _, group in grouped_data:
    selected_records.append(group.head(5))

# Concatenate the selected records into a new DataFrame
selected_df = pd.concat(selected_records)

col1,col2 =st.columns(2)

with col1:

    # Create a bar chart using Plotly
    fig = px.bar(
        top_10_stations,
        x='Trip Count',
        y='start_station_name',
        orientation='h',
        title='Top 10 Most Popular Citi Bike Stations in New York',
        labels={'start_station_name': 'Station', 'Trip Count': 'Number of Trips'},
        text='Trip Count',  # Data labels: Display trip counts on the bars
    )

    # Customize the chart layout and design
    fig.update_layout(
        xaxis_title='Number of Trips',
        yaxis_title='Station',
        yaxis_categoryorder='total ascending',  # Order the stations by trip counts
        plot_bgcolor='rgba(0,0,0,0)',  # Set the plot background color
        paper_bgcolor='rgba(0,0,0,0)',  # Set the chart background color
        font=dict(size=12),  # Adjust the font size
        margin=dict(l=50, r=50, t=80, b=50),  # Adjust the margins
    )
    # Display the bar chart using Streamlit
    st.plotly_chart(fig)


with col2:
# Add the line chart of bike trip counts and temperatures
    selected_df['temperatures_F'] = (selected_df['Avg_Temp'] * 9/5) + 32

    # Create the dual-axis line chart using Plotly
    fig = go.Figure()

    # Add bike trip counts as a line trace
    fig.add_trace(go.Scatter(x=selected_df['started_at'], y=selected_df['Trip_Count'],
                            mode='lines', name='Bike_trip_count', line=dict(color='blue'),xaxis='x1'))

    # Add temperatures as a line trace on the secondary y-axis
    fig.add_trace(go.Scatter(x=selected_df['started_at'], y=selected_df['temperatures_F'],
                            mode='lines', name='Temperature (Fahrenheit)', line=dict(color='red'),
                            yaxis='y2'))

    # Set the title and axis labels
    fig.update_layout(
        title='Bike Trip Counts and Temperatures',
        xaxis_title='Date',
        yaxis_title='Bike Trip Count',
        yaxis2=dict(title='Temperature (Fahrenheit)', overlaying='y', side='right'),
    )

    # Show the chart using Streamlit
    st.plotly_chart(fig)

# Add some additional text or information
st.write("This dashboard is designed to visualize the relationship between bike trip counts and average temperatures at different start stations in the city. The line chart shows how bike trip counts and temperatures vary over the start stations, allowing users to identify potential patterns or correlations.This dashboard also visulaize the 10 top most popular stationThis also displays the arc connects with the start and ending station and most popular trips in new york")



# Load the HTML file
html_file = open("custom_map.html", 'r', encoding='utf-8').read()
st.title("Trips with Arc Connects")

# Render the HTML file in Streamlit
st.components.v1.html(html_file, height=500)

# Load the HTML file
html_file = open("commontripmap.html", 'r', encoding='utf-8').read()
st.title("Most Common Trips with Arc Connects")

# Render the HTML file in Streamlit
st.components.v1.html(html_file, height=500)


