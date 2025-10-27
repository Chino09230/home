import streamlit as st

st.set_page_config(page_title='YAMI', page_icon='😋')
st.header("😋 震惊C神最爱的东西......")

images = ['https://img1.jiemian.com/101/original/20221111/166814582426815100_a700x398.png',
          'https://ts1.tc.mm.bing.net/th/id/R-C.fcbd5bdf7ef37663a0574ff80304555c?rik=DZAJ5%2b8dgdv%2f8w&riu=http%3a%2f%2fi5.szhomeimg.com%2fo%2f2021%2f05%2f10%2f05101648267588106.JPG&ehk=Fd6%2bov6bX%2b54HDlkIA2gjfQ4ovuffGa7ZmjEopWa6QE%3d&risl=&pid=ImgRaw&r=0',
          'https://img1.qunarzz.com/travel/poi/1505/bc/14d5bdbb0ee8d3.jpg_r_640x480x70_4935a7fb.jpg']

captions = ['面包诱惑 😘', '烤鸡 🦃', '京酱肉丝 🥩']
if 'a' not in st.session_state:
    st.session_state['a'] = 0
    
def nextimg():
    st.session_state['a'] =(st.session_state['a']+1) % len(images)
    
  
def next2mg():
    st.session_state['a'] =(st.session_state['a']-1) % len(images)


# st.image()总共两个参数，url：图片地址 caption:图片的备注
st.image(images[st.session_state['a']], captions[st.session_state['a']])



c1, c2 = st.columns(2)
with c1:
    st.button('上一张', on_click=next2mg, use_container_width=True)

with c2:
    st.button('下一张', on_click=nextimg, use_container_width=True)


