import streamlit as st
import pandas as pd
import mag4 as mg

st.write(mg.available_datasets())

st.write('Georoc Data')
st.selectbox('Name', [1,2,3])