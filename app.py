import streamlit as st
st.title("Hello,Streamlit!")
st.write("this is a simple streamlit app.")
name=st.text_input("Enter your name:")
if name:
    st.write(f"Hello,{name}!")
age=st.slider("select your age:",0,100,25) 
st.write(f"you are {age} years old.")   