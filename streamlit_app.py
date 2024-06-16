import streamlit as st

def main():
    st.title("Simple Streamlit App")
    page = st.sidebar.selectbox("Choose a page", ["Home", "About"])
    
    if page == "Home":
        st.write("This is the home page")
    elif page == "About":
        st.write("This is the about page")

if __name__ == "__main__":
    main()