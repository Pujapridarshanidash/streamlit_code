import streamlit as st
import time as t

st.title("welcome to my world")
st.header("Machine Learning")
st.subheader("Linear Regression")
st.info("Information of a User")
st.warning("Come on time or else you will be marked")
st.write("Employee Name")
st.write("range(50)")
st.error("wrong password")
st.success("congrats")
st.markdown("# my world")
st.markdown("## my world")
st.markdown("### my world")
st.markdown(":moon:")

st.text("This is a text")

st.caption("This is a caption")

st.latex(r''' a^2 + b^2 = c^2 ''')
st.checkbox("login")
st.button("Submit")
st.radio("Select your gender", ("Male", "Female", "Other"))
st.selectbox("Select your country", ("India", "USA", "UK"))
st.multiselect("Select your hobbies", ("Reading", "Traveling", "Cooking"))
st.select_slider("Select your age", options=range(1, 100))
st.slider("enter your number",0,100)
st.number_input("pick your number",0,100)
st.text_input("Enter your name email address")
st.date_input("opening ceremony")
st.time_input("Select time")
st.text_area("welcome to my python era")
st.file_uploader("Upload your file")
st.color_picker("Pick your color")
st.progress(90)
with st.spinner("Loading..."):
    
    t.sleep(2)

st.balloons()
st.sidebar.title("This is a sidebar")
st.sidebar.text_input("Enter your name")
st.sidebar.text_input("Enter your email")
st.sidebar.text_input("password")
st.sidebar.button("submit")
st.sidebar.radio("professional expert",["student","working","other"])

#data visualization
import pandas as pd
import numpy as np
st.title("bar chart")
data = pd.DataFrame(np.random.randn(50,2),columns=["a","b"])

st.bar_chart(data)
st.title("line chart")
st.line_chart(data)
st.title("area chart")
st.area_chart(data)