import streamlit as st
import pandas as pd
import webbrowser

data = pd.read_csv('https://github.com/iilyazakos/BD_PZ/blob/1984c0a0978133d4667c87880a1a4feb719c2922/data.txt?raw=true', sep=", ")
st.set_page_config(layout = "wide")
st.title('Table')
st.write(data)

if st.button('Table with calculated values'):
    webbrowser.open(f'https://iilyazakos-bd-pz-app-table-5sk2b1.streamlit.app')
