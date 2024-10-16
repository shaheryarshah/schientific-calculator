# calculator_app.py

import streamlit as st
import math

def main():
    st.title("Scientific Calculator")

    # Input numbers and operations
    st.header("Basic Operations")
    num1 = st.number_input("Enter the first number", value=0.0, format="%.2f")
    num2 = st.number_input("Enter the second number", value=0.0, format="%.2f")

    # Choose an operation
    operation = st.selectbox("Choose an operation", ["Add", "Subtract", "Multiply", "Divide"])

    # Basic calculations
    if operation == "Add":
        result = num1 + num2
    elif operation == "Subtract":
        result = num1 - num2
    elif operation == "Multiply":
        result = num1 * num2
    elif operation == "Divide":
        result = num1 / num2 if num2 != 0 else "Cannot divide by zero"

    st.write("Result of {} is: {}".format(operation, result))

    # Scientific operations on a single number
    st.header("Scientific Operations")
    num = st.number_input("Enter a number for scientific operations", value=0.0, format="%.2f")
    sci_operation = st.selectbox(
        "Choose a scientific operation",
        ["Square", "Square Root", "Sine", "Cosine", "Tangent", "Logarithm (Base 10)", "Exponential"]
    )

    # Advanced calculations
    if sci_operation == "Square":
        sci_result = num ** 2
    elif sci_operation == "Square Root":
        sci_result = math.sqrt(num)
    elif sci_operation == "Sine":
        sci_result = math.sin(math.radians(num))
    elif sci_operation == "Cosine":
        sci_result = math.cos(math.radians(num))
    elif sci_operation == "Tangent":
        sci_result = math.tan(math.radians(num))
    elif sci_operation == "Logarithm (Base 10)":
        sci_result = math.log10(num) if num > 0 else "Undefined for non-positive values"
    elif sci_operation == "Exponential":
        sci_result = math.exp(num)

    st.write("Result of {} is: {}".format(sci_operation, sci_result))

if __name__ == "__main__":
    main()
