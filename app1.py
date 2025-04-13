import streamlit as st
import pandas as pd 
import os
from io import bytesIO


#set up our app
st.set_page_config(page_title="Data Sweeper",layout='wide')
st.title("Data Sweeper")
st.write("Tranform your file between csv and excel formates with built-in data cleaning and visualization") 

uploaded_files = st.file_uploader ("upload your file between (csv and excell):", type=["csv","xlsx"], accept_multiple_files=True)
if uploaded_files:
    for file in uploaded_files:
        file_ext = os.path.splittext(file.name)[-1].lower()

        if file_ext == ".csv":
            df =pd.read_csv(file)
        elif file_ext == ".xlsx":
            df = pd.read_excel(file)
        else:
            st.error("Unsported file type:{file_ext}")
            continue 






import streamlit as st

name = st.text_input("Enter Your Name: ")
fname = st.text_input("Enter Your Father Name: ")
adr = st.text_input("Enter Your Text")
classdata = st.selectbox("Enter Your Class: ",(1,2,3,4,5,6))

button = st.button("Done")
if button :
    st.markdown(f"""
    Name : {name}
    Father Nmae : {fname}
    address : {adr}
    class : {classdata}
    
""")