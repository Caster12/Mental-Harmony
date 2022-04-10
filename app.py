import numpy as np
import streamlit as st
import ha
import mental

PAGES = {
    "Mental healthcare chatbot": mental ,
    "Mental disease": ha 
}
st.sidebar.title('Mental Harmony')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()