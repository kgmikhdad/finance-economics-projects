# app.py
import streamlit as st

def main():
    st.title("Simple Streamlit App")
    st.write("Welcome to this simple Streamlit app!")
    
    user_input = st.text_input("Enter your name:", "John Doe")
    st.write(f"Hello, {user_input}!")

if __name__ == "__main__":
    main()
