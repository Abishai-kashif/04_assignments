import streamlit as st

st.title("BMI Calculator")

# User inputs
height = st.number_input("Enter your height in meters", min_value=0.0, step=0.01)
weight = st.number_input("Enter your weight in kilograms", min_value=0.0, step=0.1)

if st.button("Calculate BMI"):
    if height > 0:
        bmi = weight / (height ** 2)
        st.write(f"Your BMI is: {bmi:.2f}")
        if bmi < 18.5:
            st.write("You are underweight.")
        elif 18.5 <= bmi < 25:
            st.write("Your weight is normal.")
        elif 25 <= bmi < 30:
            st.write("You are overweight.")
        else:
            st.write("You are obese.")
    else:
        st.write("Please enter a valid height.")