import streamlit as st
import pandas as pd

st.title('Sales Analysis App')

uploaded_file = st.file_uploader("Choose an Excel file", type="xlsx")

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    st.write("Top 5 rows of the table:")
    st.write(df.head())
