'''
how to run
- open terminal
- cd app1
- sreamlit run main.py
'''
import streamlit as st
st.title ("This is a title")
st.header ("This is a header")
st.subheader ("This is a subheader")
st.text ("A very normal text on a normal day")
st.write('This is the magic function to write text')
st.success("This is text written for success messages")
st.error("This is text written for error messages")
st.info('This is information message text')
st.warning('This is warning message text')
st.markdown('''
This is a markdown text,here u are free to use
<h5>HTcd app1ML <h5>
<p>this is a paragraph</p>
<ul>
<li>One Two</li>
<li>Three Four</li>
<li>Five Six</li>
</ul>
or 
# Markdown heading
''',unsafe_allow_html=True)

st.code('area where we can put code')