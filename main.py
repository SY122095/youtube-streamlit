import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

# タイトルの表示
st.title('Streamlit 超入門')

# テキストの追加
st.write('DataFrame')

df = pd.DataFrame({
    '1列目': [1, 2, 3, 4],
    '2列目': [10, 20, 30, 40]
})
# st.dataframe(df.style.highlight_max(axis=0), width=1000, height=1000) # highlight_max: 最大値を強調

df2 = pd.DataFrame(
    np.random.rand(20, 3), # 一様分布 (行, 列)
    columns= ['a', 'b', 'c']
)

# チャートの描画
st.bar_chart(df2)


df3 = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
    columns=['lat', 'lon']
)

# マッピング
st.map(df3)

# 画像の表示
st.write('Display Image')
img = Image.open('C:\\Users\\yhfhg\\OneDrive\\デスクトップ\\streamlit\\mlb.jpg')
st.image(img, caption='MLB', use_column_width=True)