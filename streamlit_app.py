import streamlit as st
import pandas as pd
import mag4 as mg
import matplotlib.pyplot as plt

data = mg.available_datasets()
st.write(data)
#df = mg.get_data('Bastar Craton')
#st.write(df)
st.write('Georoc Data')
sel_data = st.selectbox('Name', data['Title'])
st.write(sel_data)
test = mg.get_data(sel_data)

Elemente = test.columns.tolist()[27:]
El1= st.selectbox('x-Achse', Elemente )
El2= st.selectbox('y-Achse', Elemente)

plt.scatter(test[El1], test[El2])
st.pyplot(plt)


