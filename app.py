import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Title
st.title("Scientific and Graphical Calculator")

# Sidebar for selection
st.sidebar.title("Calculator Options")
operation = st.sidebar.selectbox(
    "Choose Operation",
    ["Basic Operations", "Scientific Operations", "Graphing"]
)

# Basic Operations
if operation == "Basic Operations":
    st.header("Basic Calculator")
    num1 = st.number_input("Enter first number", format="%f")
    num2 = st.number_input("Enter second number", format="%f")
    basic_op = st.selectbox("Select an operation", ["Add", "Subtract", "Multiply", "Divide"])
    
    if st.button("Calculate"):
        if basic_op == "Add":
            result = num1 + num2
        elif basic_op == "Subtract":
            result = num1 - num2
        elif basic_op == "Multiply":
            result = num1 * num2
        elif basic_op == "Divide":
            result = num1 / num2 if num2 != 0 else "Undefined (Division by Zero)"
        st.success(f"Result: {result}")

# Scientific Operations
elif operation == "Scientific Operations":
    st.header("Scientific Calculator")
    sci_num = st.number_input("Enter a number for scientific calculation", format="%f")
    sci_op = st.selectbox(
        "Select a scientific operation",
        ["Sin", "Cos", "Tan", "Log (base 10)", "Exponential", "Square Root"]
    )
    
    if st.button("Compute"):
        if sci_op == "Sin":
            result = np.sin(np.radians(sci_num))
        elif sci_op == "Cos":
            result = np.cos(np.radians(sci_num))
        elif sci_op == "Tan":
            result = np.tan(np.radians(sci_num))
        elif sci_op == "Log (base 10)":
            result = np.log10(sci_num) if sci_num > 0 else "Undefined (Log of non-positive number)"
        elif sci_op == "Exponential":
            result = np.exp(sci_num)
        elif sci_op == "Square Root":
            result = np.sqrt(sci_num) if sci_num >= 0 else "Undefined (Square root of negative number)"
        st.success(f"Result: {result}")

# Graphing Features
elif operation == "Graphing":
    st.header("Graphing Calculator")
    function = st.text_input("Enter a mathematical function (e.g., sin(x), x**2, log(x))")
    x_min = st.number_input("Enter minimum x value", format="%f")
    x_max = st.number_input("Enter maximum x value", format="%f")
    
    if st.button("Plot"):
        try:
            x = np.linspace(x_min, x_max, 500)
            y = eval(function)
            plt.figure(figsize=(8, 6))
            plt.plot(x, y, label=function, color='green')
            plt.title("Graph")
            plt.xlabel("x-axis")
            plt.ylabel("y-axis")
            plt.legend()
            plt.grid(True)
            st.pyplot(plt)
        except Exception as e:
            st.error(f"Error in plotting: {e}")

