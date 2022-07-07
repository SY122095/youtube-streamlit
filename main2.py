import streamlit as st
import numpy as np
import pandas as pd
import time
from PIL import Image

# Everything is accessible via the st.secrets dict:

st.write("DB username:", st.secrets["db_username"])
st.write("DB password:", st.secrets["db_password"])
st.write("My cool secrets:", st.secrets["my_cool_secrets"]["things_i_like"])

# And the root-level secrets are also accessible as environment variables:

import os

st.write(
    "Has environment variables been set:",
    os.environ["db_username"] == st.secrets["db_username"],
)

# Streamlitの実行
# streamlit run -----.py

# タイトルの表示
st.title('Streamlit 超入門')

st.write('プログレスバーの表示')
'Start!!'
latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i+1)
    time.sleep(0.1)
'Done!'


st.write('Interactive Widgets')
left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander = st.expander('問い合わせ')
expander.write('問い合わせ内容を書く')

text = st.text_input('あなたの趣味を教えてください。')
condition = st.slider('あなたの今の調子は？', 0, 100, 50)

'あなたの趣味は', text, 'です。'
'コンディション: ', condition

option = st.selectbox(
    'あなたが好きな数字を教えてください。',
    list(range(1, 11))
)
'あなたの好きな数字は、', option, 'です。'

if st.checkbox('Show Image'):
    img = Image.open('C:\\Users\\yhfhg\\OneDrive\\デスクトップ\\streamlit\\mlb.jpg')
    st.image(img, caption='MLB', use_column_width=True)
