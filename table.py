import streamlit as st
import pandas as pd
import webbrowser

data = pd.read_csv('data.txt', sep=", ")
st.set_page_config(layout = "wide")
st.title('Table')
st.write(data)

if st.button('Table with calculated values'):
    webbrowser.open_new_tab('https://iilyazakos-bd-pz-app-table-5sk2b1.streamlit.app/')
