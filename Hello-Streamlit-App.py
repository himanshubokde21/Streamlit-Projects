import streamlit as st

st.title("👋 Hello Streamlit App")
st.markdown("A <span style='color: lightblue; font-size: 19px; font-weight: bolder;'>Hello Streamlit</span> app that displays your name, age, and a short bio.", unsafe_allow_html=True)

name = st.text_input("Name: ", placeholder="Enter your Name", help="you have to enter your 'name' here")
age = st.number_input("Age: ", placeholder="Enter your Age", help="you have to enter your 'age' here")
bio = st.text_area("Bio: ", placeholder="Enter your Bio", help="you have to enter your 'bio' here")

if name and age and bio:
    st.markdown("<h4 style='color:orange;'>🌟 Your Information 🌟</h4>", unsafe_allow_html=True)
    st.write("👋 Hello, ", name)
    st.write("🌟 Age : ", age)
    st.write("🧠 Bio : ", bio)

    
