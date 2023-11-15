import csv
import os
import django
import pandas as pd
from IPython.display import display
from PIL import Image

base_url = "https://data.taipower.com.tw/opendata/apply/file/d007012/%E5%8F%B0%E7%81%A3%E9%9B%BB%E5%8A%9B%E5%85%AC%E5%8F%B8_%E5%90%84%E7%B8%A3%E5%B8%82%E4%BD%8F%E5%AE%85%E3%80%81%E6%9C%8D%E5%8B%99%E6%A5%AD%E5%8F%8A%E6%A9%9F%E9%97%9C%E7%94%A8%E9%9B%BB%E7%B5%B1%E8%A8%88%E8%B3%87%E6%96%99.csv"
df_raw = pd.read_csv(base_url, encoding='UTF-8')

# 複製一份做處理
df = df_raw.copy()

df = df.drop(columns=['住宅部門用電佔比(%)','服務業部門(含包燈)(度)','服務業部門(含包燈)用電佔比(%)','農林漁牧售電量(度)','農林漁牧用電佔比(%)','工業部門用電佔比(%)','縣市用電佔比(%)'])
# 顯示結果
display(df)