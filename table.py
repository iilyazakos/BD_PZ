import streamlit as st
from bokeh.models.widgets import Div
import pandas as pd

def open_link(url, new_tab=True):
    if new_tab: js = f"window.open('{url}')"
    else: js = f"window.location.href = '{url}'"
    html = '<img src onerror="{}">'.format(js)
    div = Div(text = html)
    st.bokeh_chart(div)


data = pd.read_csv('data.txt', sep=", ")
st.set_page_config(layout = "wide")
st.title('Table')
st.write(data)
