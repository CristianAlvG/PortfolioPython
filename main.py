import streamlit as st
import pandas

st.set_page_config(layout="wide", page_title="Cristian's Portfolio")

col1, col2 = st.columns(2)


with col1:
    st.image("images/photo.png", width=550)

with col2:
    st.title("Cristian Adrian")
    content = """
    Hi Im Cristian! I am a Python programmer, Born in Costa Rica, I usually enjoy playing music, 
    hanging around with friends, going to the mountains, and cooking, I am 25 years old, and 
    in a few months ill be searching for a Job. I love Worships and I usually sing in my Church 
    Oasis de Esperanza. My favorite hobie is playing the piano, and also programing, 
    I enjoy developing Web applications and Python applications, I have great social
    abilities, and lots of friends, Im not frightened to the the challenges that are 
    coming every day, Im Christian so I believe in God, and He is giving me the wisdom
    to develop applications and thriving me in everything I do 
    """
    st.info(content)

content2 = """Below you can find some of the apps I have built in Python. Feel free to contact me"""

st.write(content2)

df = pandas.read_csv("data.csv", sep=";")

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")