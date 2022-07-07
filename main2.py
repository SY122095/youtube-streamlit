import streamlit as st
import numpy as np
import pandas as pd
import time
from PIL import Image
import hashlib


SALT = 'aiueo:'
# 'password' をハッシュ化したもの
HASHED_PASSWORD = '246380e2b28d0898ff4b214ced62e851fee242112ae9a01a6ab49216194c0d7a'


def get_hash(password):
    return hashlib.sha256((SALT + password).encode('utf-8')).hexdigest()


def check_password(password, hashed_password):
    return get_hash(password) == hashed_password


def login():
    placeholder = st.empty()
    with placeholder.form('login'):
        password = st.text_input('パスワード', type='password')
        st.form_submit_button('ログイン')

    if check_password(password, HASHED_PASSWORD):
        placeholder.empty()
        return True
    else:
        if password:
            st.write('パスワードが違います')
        return False


def main():
    loggedin = login()
    if loggedin:
        st.write('Authenticated!')
            

if __name__ == '__main__':
    main()

# Streamlitの実行
# streamlit run -----.py

# タイトルの表示
if check_password(password, HASHED_PASSWORD):
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
