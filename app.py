
import streamlit as st
import pandas as pd


import json
import matplotlib.pyplot as plt
import matplotlib
from text_data_analysis import analysis
from documentation import docs




menuItems = [
    'Text Data Analysis',
    'Automatic Data Analysis',
    
    'Documentation']
st.sidebar.title('Easy Analysis')


itemSelected = st.sidebar.selectbox('', menuItems)
github = '''[ Fork/Star on Github](https://github.com/rishavrajjain/felix)'''
st.sidebar.info(github)

if itemSelected == 'Text Data Analysis':
    
    st.title('Text Data Analysis')
    analysis()
    

    

    

elif itemSelected == 'Automatic Data Analysis':
    st.title('Automatic Data Analysis')

    data = st.file_uploader("Upload a Dataset", type=["csv"])
    if data is not None:
        df = pd.read_csv(data)
        st.dataframe(df)
        st.write('Shape')
        st.write(df.shape)
        all_columns = df.columns.to_list()
        st.write('Columns')
        st.write(all_columns)

        st.write('Summary of the Data')
        st.write(df.describe())

        

        if st.checkbox("Plot data for a column"):
            selected_column = st.selectbox("Select Columns", all_columns)
            new_df = df[selected_column]
            st.dataframe(new_df.value_counts())
            st.bar_chart(new_df.value_counts())

        if st.checkbox("Advance Plots and Analysis"):

            all_columns_names = df.columns.tolist()
            type_of_plot = st.selectbox(
                "Select Type of Plot", [
                    "area", "bar", "line"])
            selected_columns_names = st.multiselect(
                "Select Columns To Plot", all_columns_names)
            if st.button("Generate Plot"):
                st.success(
                    "Generating Customizable Plot of {} for {}".format(
                        type_of_plot, selected_columns_names))

                # Plot By Streamlit
                if type_of_plot == 'area':
                    cust_data = df[selected_columns_names]
                    st.area_chart(cust_data)

                elif type_of_plot == 'bar':
                    cust_data = df[selected_columns_names]
                    st.bar_chart(cust_data)

                elif type_of_plot == 'line':
                    cust_data = df[selected_columns_names]
                    st.line_chart(cust_data)

                


if itemSelected == 'Documentation':
    st.title('Documentation')
    st.markdown(docs())
    
