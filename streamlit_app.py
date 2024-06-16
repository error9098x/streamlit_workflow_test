import streamlit as st

def main():
    st.title("Simple Streamlit App")
    page = st.sidebar.selectbox("Choose a page", ["Home", "About"])
    
    if page == "Home":
        st.write("This is the home page")

        st.write("this")
        st.write("This is a test")

    elif page == "About":
        st.write("This is the about page")
        st.write("This is a sample change for the PR.") 

if __name__ == "__main__":
    main()
