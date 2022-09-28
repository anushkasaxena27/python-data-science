import streamlit as st
st.title('Simple Form')
with st.form('MyForm'):
    name = st.text_input('Enter your name')
    age = st.number_input('Enter your age',min_value=18,max_value=90)
    message = st.text_area('Enter your thoughts')
    time = st.time_input('Enter what time')
    date = st.date_input('Enter the date')
    file = st.file_uploader('Select a file')
    camera = st.camera_input('Grab a photo from webcam')
    sb = st.form_submit_button('Submit')
if sb:
    st.write (name)
    st.write (age)
    st.write (message)
    st.write (time)
    st.write (date)
    st.write (file)
    st.write (camera)

with st.form ('Another Form'):
    color = st.color_picker('Pick a color')
    num1 = st.select_slider('Select a value',[1,2,3,4,5,6,7,8,9,10])
    num2 = st.slider('Select another value',min_value=25,max_value=100)
    gender = st.radio('Gender',['Male','Female','Other'],horizontal= True)
    education = st.selectbox('Select your highest education',['Intermediate',
    'High School','Graduate','Master','Padhe likhe gawar'])
    likes = st.multiselect('Select what u like',['Maggi','Pizza','Burger','Biryani','Spinach','Pasta','Dry Fruits',"🍒"])
    checked = st.checkbox("Agree to our secret terms and conditions",value = True)
    submit = st.form_submit_button('Submit')
 