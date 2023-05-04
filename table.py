import streamlit as st
import pandas as pd
from bokeh.models.widgets import Div

data = pd.read_csv('https://github.com/iilyazakos/BD_PZ/blob/1984c0a0978133d4667c87880a1a4feb719c2922/data.txt?raw=true', sep=", ")
st.set_page_config(layout = "wide")
st.title('Table')
st.write(data)

if st.button('Table with calculated values'):
    js = "window.open('https://iilyazakos-bd-pz-app-table-5sk2b1.streamlit.app/')"  # New tab or window
    html = '<img src onerror="{}">'.format(js)
    div = Div(text=html)
    st.bokeh_chart(div)
