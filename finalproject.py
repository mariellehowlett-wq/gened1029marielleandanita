import streamlit as st
import time

st.title("Human Differences Explorer")

st.write("Click an option to learn about different types of human variation.")

option = st.radio(
    "Choose a category:",
    ["Height", "Skin Tone", "Hair Type", "Eye Color", "Genetics"]
)

if option == "Height":
    st.subheader("Height")
    st.write("Height differs among humans because of genetics, nutrition, health, and environment.")

    for i in range(120, 201, 10):
        st.progress((i - 120) / 80)
        st.write(f"Example height: {i} cm")
        time.sleep(0.1)

elif option == "Skin Tone":
    st.subheader("Skin Tone")
    st.write("Skin tone varies mainly because of melanin, a pigment that helps protect skin from UV radiation.")

elif option == "Hair Type":
    st.subheader("Hair Type")
    st.write("Hair texture can be straight, wavy, curly, or coily. This is influenced by genetics and hair follicle shape.")

elif option == "Eye Color":
    st.subheader("Eye Color")
    st.write("Eye color depends on the amount and type of pigment in the iris.")

elif option == "Genetics":
    st.subheader("Genetics")
    st.write("Humans are genetically very similar, but small genetic differences contribute to traits like height, hair, and eye color.")
