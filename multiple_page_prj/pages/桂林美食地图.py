import streamlit as st
import pandas as pd
import random
import time

st.header("❤ 桂林TOP5本人最爱 ❤")

st.text('麦香坊|椿记烧鹅|桂小厨|酒拾烤肉|绿茶餐厅')

map_data = {
    'latitude':[25.281724,25.257572,25.262201,25.248653,25.262203],
    'longitude':[110.301915,110.222554,110.269705,110.168359,110.268694],
    }

st.header("📍 桂林美食地图 📍")

st.map(pd.DataFrame(map_data))

data = {
    '用餐时间':['11', '12', '13','17','18','19','20'],
    '麦香坊':[30, 60, 54, 34, 45, 58, 28],
    '椿记烧鹅':[36, 71, 50, 35, 88, 65, 44],
    '桂小厨':[17, 50, 32, 40, 55, 43, 20],
    '酒拾烤肉':[22,65,45,50,33,50,60],
    '绿茶餐厅':[35,55,44,33,71,76,50]
}

df = pd.DataFrame(data)

index = pd.Series([1, 2, 3, 4, 5, 6, 7], name='序号')

df.index = index

st.header("🚶用餐时间人流量🚶")

st.area_chart(df, x='用餐时间')

st.subheader('当前人流量')
progress_text_1 ="正在统计"
my_bar = st.progress(0,text=progress_text_1)
time.sleep(0.5)
for precent in range(80):
    time.sleep(0.1)
    my_bar.progress(precent+1,text=f'{precent}%:拥挤:')

data1 = {
    '价格':['早餐','午餐','晚餐','宵夜'],
    '麦香坊':[20,40,55,35],
    '椿记烧鹅':[50,70,75,50],
    '桂小厨':[35,55,65,60],
    '酒拾烤肉':[22,65,45,50],
    '绿茶餐厅':[35,55,60,45]
}

df1 = pd.DataFrame(data1)
index1 = pd.Series([1, 2, 3, 4,], name='序号')
df1.index = index1

month_order = ['早餐','午餐','晚餐','宵夜']

df1['价格'] = pd.Categorical(df1['价格'], categories=month_order, ordered=True)

df1_sorted = df1.sort_values('价格').set_index('价格')

st.header("💰 不同类型餐厅价格 💰")

st.line_chart(df1, x='价格')

data2 = {
    '店铺':['麦香坊','椿记烧鹅','桂小厨', '酒拾烤肉', '绿茶餐厅'],
    '评分':[4.6,4.1,4,4.5,4.3]
} 

df2 = pd.DataFrame(data2)

index2 = pd.Series([1,2,3,4,5,], name='')

df2.index = index2

st.header("⭐ 餐厅评分 ⭐")

st.bar_chart(df2, x='店铺')

data3 = {
    '月份': ['一月', '二月', '三月', '四月', '五月', '六月', '七月', '八月', '九月', '十月', '十一月', '十二月'],
    '麦香坊': [50,55,60,66,70,73,78,75,89,99,92,90],
    '椿记烧鹅': [70,80,90,85,74,88,99,93,88,77,96,99],
    '桂小厨': [40,49,54,60,58,64,60,75,85,92,91,98],
    '酒拾烤肉': [42,48,52,54,58,66,77,89,91,99,85,92],
    '绿茶餐厅': [55,60,58,66,67,78,88,92,98,96,99,95]
}
df3 = pd.DataFrame(data3)

index3 = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], name='序号')

df3.index = index3

month_order = ['一月', '二月', '三月', '四月', '五月', '六月', '七月', '八月', '九月', '十月', '十一月', '十二月']

df3['月份'] = pd.Categorical(df3['月份'], categories=month_order, ordered=True)

st.header("💸 今年各餐厅营业额 💸")

df3_sorted = df3.sort_values('月份').set_index('月份')


st.line_chart(df3_sorted)

img_list = ["https://ts1.tc.mm.bing.net/th/id/OIP-C.ldUbad0bkLsnmQ23g0eOYQHaE8?w=299&h=204&c=8&rs=1&qlt=90&o=6&cb=12&pid=3.1&rm=2", "https://ts1.tc.mm.bing.net/th/id/OIP-C.pE5bkLcIR3A2R71OBO9nVQHaGH?w=241&h=204&c=8&rs=1&qlt=90&o=6&cb=12&pid=3.1&rm=2", "https://ts1.tc.mm.bing.net/th/id/OIP-C.Yx1KKVfhuodK4IluqqGuKgHaE7?w=299&h=204&c=8&rs=1&qlt=90&o=6&cb=12&pid=3.1&rm=2","https://www.china-greentea.com.cn/uploads/upload/images/20250120/dd1a4ae024a7c75bc2169d0530e7e9dd.jpg","https://img1.qunarzz.com/travel/d3/1809/68/90e7cff1437c7fb5.jpg"]

st.title("🎲 今天吃什么 🎲")

if st.button("看看吃啥吧"):
    random_img = random.choice(img_list)
    st.image(random_img, caption=f"Delicious Food", use_container_width=True)
else:
    st.image(img_list[0], caption="Delicious Food", use_container_width=True)

