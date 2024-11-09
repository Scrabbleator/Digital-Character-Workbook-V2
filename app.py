import streamlit as st

# Import the Basic Profile section
from basic_profile import basic_profile_section

# Title and Description
st.title("Digital Character Workbook")
st.markdown("Welcome to the Digital Character Workbook. Follow each section to develop your character in depth.")

# Display Basic Profile Section
st.header("Basic Profile")
basic_profile_section()
