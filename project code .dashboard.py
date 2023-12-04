import streamlit as st
import pandas as pd
import plotly.express as px

file_path = r"C:\Users\siras\Downloads\archive (12)\Construction_Data_PM_Forms_All_Projects.csv"
df = pd.read_csv(file_path)

st.title('Construction Data Dashboard')
st.write(df)

st.sidebar.title('User Interaction')
selected_project = st.sidebar.selectbox('Select Project', ['All'] + list(df['Project'].unique()))
if selected_project != 'All':
    filtered_df = df[df['Project'] == selected_project]
else:
    filtered_df = df

open_actions_range = st.sidebar.slider('Filter by Open Actions', min_value=0, max_value=10, value=(0, 10))
total_actions_range = st.sidebar.slider('Filter by Total Actions', min_value=0, max_value=10, value=(0, 10))

filtered_df = filtered_df[
    (filtered_df['Open Actions'] >= open_actions_range[0]) & (filtered_df['Open Actions'] <= open_actions_range[1])]
filtered_df = filtered_df[
    (filtered_df['Total Actions'] >= total_actions_range[0]) & (filtered_df['Total Actions'] <= total_actions_range[1])]

# Use columns to place charts in rows
col1, col2, col3 = st.columns(3)

# Row 1
with col1:
    st.subheader('Line Chart - Total Actions Over Time')
    line_chart = px.line(filtered_df, x='Ref', y='Total Actions', title='Total Actions Over Time',
                         labels={'Total Actions': 'Total Actions'})
    st.plotly_chart(line_chart, use_container_width=True)

with col2:
    st.subheader('Bar Chart - Total Actions by Type')
    bar_chart = px.bar(filtered_df, x='Type', y='Total Actions', title='Total Actions by Type',
                       labels={'Total Actions': 'Total Actions'})
    st.plotly_chart(bar_chart, use_container_width=True)

with col3:
    st.subheader('Pie Chart - Distribution of Status')
    pie_chart = px.pie(filtered_df, names='Status', title='Distribution of Status')
    st.plotly_chart(pie_chart, use_container_width=True)

# Row 2
with col1:
    st.subheader('Scatter Plot - Open Actions vs. Total Actions')
    scatter_plot = px.scatter(filtered_df, x='Open Actions', y='Total Actions', color='Status',
                              title='Open Actions vs. Total Actions')
    st.plotly_chart(scatter_plot, use_container_width=True)

with col2:
    st.subheader('Sunburst Chart - Project and Status Hierarchy')
    sunburst_chart = px.sunburst(filtered_df, path=['Project', 'Status'], title='Project and Status Hierarchy')
    st.plotly_chart(sunburst_chart, use_container_width=True)

with col3:
    st.subheader('Violin Plot - Open Actions by Type')
    violin_plot = px.violin(filtered_df, x='Type', y='Open Actions', title='Open Actions by Type',
                            labels={'Open Actions': 'Open Actions'})
    st.plotly_chart(violin_plot, use_container_width=True)

# Row 3
with col1:
    st.subheader('Area Chart - Cumulative Total Actions Over Time')
    filtered_df['Cumulative Total Actions'] = filtered_df['Total Actions'].cumsum()
    area_chart = px.area(filtered_df, x='Ref', y='Cumulative Total Actions',
                         title='Cumulative Total Actions Over Time',
                         labels={'Cumulative Total Actions': 'Cumulative Total Actions'})
    st.plotly_chart(area_chart, use_container_width=True)

with col2:
    st.subheader('Histogram - Distribution of Total Actions')
    histogram = px.histogram(filtered_df, x='Total Actions', nbins=20,
                             title='Distribution of Total Actions',
                             labels={'Total Actions': 'Total Actions'})
    st.plotly_chart(histogram, use_container_width=True)

with col3:
    st.subheader('3D Scatter Plot - Open Actions, Total Actions, and Type')
    scatter_3d = px.scatter_3d(filtered_df, x='Open Actions', y='Total Actions', z='Type', color='Status',
                              title='3D Scatter Plot - Open Actions, Total Actions, and Type')
    st.plotly_chart(scatter_3d, use_container_width=True)
