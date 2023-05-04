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

s = 0
for i in range(0, 7):
    s = data["tax"][i]*(data["cost(rub)"][i]*data["avg"][i])+s

f = 0
for i in range(0, 7):
  f = f+data["cost(rub)"][i]*data["avg"][i]

data['avg_cost'] = data['avg'] * data['cost(rub)']
data['price(rub)'] = round((data['avg_cost']*(1+data['tax'])+data['delivery(rub)']), 2)

sums = pd.Series(["Сумма:", "", data["avg"].sum(),
                  f,
                  "", round(s, 2),
                  data["delivery(rub)"].sum(),
                 "", ""],
                 index=data.columns)
data = data.append(sums, ignore_index=True)

finish = pd.Series(["Итог:", f+s+data["delivery(rub)"].sum(), " ", " ", " ", " ", " ", " ", " " ], index=data.columns)

data = data.append(finish, ignore_index=True)

st.write(data)
