import streamlit as st
import pandas as pd
from bokeh.models.widgets import Div

data = pd.read_csv('https://github.com/iilyazakos/BD_PZ/blob/1984c0a0978133d4667c87880a1a4feb719c2922/data.txt?raw=true', sep=", ")
st.set_page_config(layout = "wide")
st.title('Table with calculated values')
s = 0
for i in range(0, 7):
    s = data["tax"][i]*(data["cost(rub)"][i]*data["avg"][i])+s
f = 0
for i in range(0, 7):
  f = f+data["cost(rub)"][i]*data["avg"][i]

data['avg_cost'] = data['avg'] * data['cost(rub)']
data['price(rub)'] = round((data['avg_cost']*(1+data['tax'])+data['delivery(rub)']), 2)
sums = pd.DataFrame([[str('Amount:'), "", data["avg"].sum(), "", "", round(s, 2), data["delivery(rub)"].sum(),f, ""]], columns=data.columns)


data = pd.concat([data, sums])
finish = pd.DataFrame([[str('Result:'), round((f+s+data["delivery(rub)"].sum()), 2), "", "", "", "", "", "", ""]], columns=data.columns)
data = pd.concat([data, finish], ignore_index=True)
st.write(data)

if st.button('Return to original page'):
    js = "window.open('https://iilyazakos-bd-pz-table-5vxp5y.streamlit.app/')"  # New tab or window
    html = '<img src onerror="{}">'.format(js)
    div = Div(text=html)
    st.bokeh_chart(div)
