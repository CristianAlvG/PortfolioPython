import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png", width=550)

with col2:
    st.title("Cristian Alvarez")
    content = """
    Hi Im Cristian! I am a Python programmer, I usually enjoy playing music, hanging around with friends,
    going to the mountains, and cooking, I am 25 years old, and in a few months ill be searching for a 
    Job. I love Worships and I usually sing in my Church Oasis de Esperanza.
    """
    st.info(content)
