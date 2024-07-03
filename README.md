
df_db= gcc.display_databases(
fil = df_db['type'] == 'georoc'
st.write(gcc.get_data(df_db[fil]['available datasets'].tolist()[0]).columns.tolist()[27:])

col1, col2 = st.columns(2)

with col1:
sel_dataset = st.selectbox(
   'How would you like to be contracted?',
   df_db[fil]['available datasets'])
x_axis = st.selectbox('select x-axis', elements)
y_axis = st.selectbox('select y-axis', elements)

with col2:
x= gcc.get_data(sel_dataset)[x_axis]/10000
y= st.write(gcc.get_data(sel_dataset)[y_axis]/10000)
p= figure(
   title: 'simple line example',
   x_axis_label= x_axis + '(wt%)',
   y_axis_label= y_axis + '(wt%)'
)
p.scatter(x_axis, y_axis, legend_label= sel_dataset)

with st.expander('See explanation'):
wt.write('The chart aboce shows soe numbers I picked for you:')
st.write('You selected:', sel_dataset)
st.write(df_db[fil])
st.dataframe(gcc.get_data('Banda Arc'))