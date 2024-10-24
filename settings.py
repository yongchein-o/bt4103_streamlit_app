import streamlit as st
import pandas as pd
import plotly.express as px
import hashlib
import os

# st.header("Selections")
# st.write(f"Your selections are {st.session_state.selections}.")

# def columns_array_creator(total_number, max_column_per_row):
#     columns_array = []
#     count = 0
#     while(count + max_column_per_row < total_number):
#         count += max_column_per_row
#         columns_array.append(max_column_per_row)
#     if(total_number - count > 0):
#         columns_array.append(total_number - count)
#     return columns_array

# selections = st.session_state.selections
# unique_values = set(item.split(" - ")[0] for item in selections)
# unique_count = len(unique_values)

# outer_columns_array = columns_array_creator(unique_count, 2)
# st.write(outer_columns_array)

@st.cache_data
def load_data(file_path='data.xlsx'):
    return pd.read_excel(file_path, sheet_name='data')

df = load_data()



def create_line_chart(parent_container, key):
    child_container = parent_container.container()
    col1, col2 = child_container.columns(2)
    x_axis = col1.selectbox(label="X axis variable", options=["CreateDate", "Price"], index=0, key=key+"line_x_axis")
    y_axis = col2.selectbox(label="Y axis variable", options=["Value", "Quantity"], index=0, key=key+"line_y_axis")
    fig = px.line(df, x=x_axis, y=y_axis, title=f'Line Chart of {y_axis} vs {x_axis}')
    child_container.plotly_chart(fig, key=key+"line")


def create_pie_chart(parent_container, key):
    child_container = parent_container.container()
    #col1, col2 = child_container.columns(2)
    #variable = col1.selectbox(label="Variable", options=["Order Capacity",], index=0)
    variable = child_container.selectbox(label="Variable", options=["OrderCapacity", "Exchange"], index=0, key=key+"pie_var")
    fig = px.pie(df, values='Price', names=variable, title=f'Pie Chart of {variable}')
    child_container.plotly_chart(fig, key=key+"pie")
    

col1, col2 = st.columns(2)
chart_type_1 = col1.selectbox(label="Chart type", options=["Line Chart", "Pie Chart"], index=0)
chart_type_2 = col2.selectbox(label="Chart type", options=["Line Chart", "Pie Chart"], index=1)

match chart_type_1:
    case "Line Chart": create_line_chart(col1, "1")
    case "Pie Chart": create_pie_chart(col1, "1")

match chart_type_2:
    case "Line Chart": create_line_chart(col2, "2")
    case "Pie Chart": create_pie_chart(col2, "2")

    


# col1, col2, col3 = st.columns(3)  # Columns are containers
# # overview_container = st.container(border=True, key="overview_container")
# metrics_container = st.container(key="metrics_container")


# overview_container = col1.container(border=True)
# overview_expander = overview_container.expander("More Details")
# overview_expander.write("ZM insert your report here")


# with col1:
    


#     # with overview_container:
#     with metrics_container:
#         col_a, col_b, col_c = st.columns(3)
#         with col_a:
#             st.metric("Total Number of Orders", "5K")

#         with col_b:
#             st.metric("Total Volume of Orders", "40.39M")

#         with col_c:
#             st.metric("Total Value of Orders", "$33.28M")
#     with st.expander("More Details"):
#         st.write('''
#             ZM insert your report here.
#         ''')

            