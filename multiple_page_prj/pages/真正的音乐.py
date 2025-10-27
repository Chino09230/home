import streamlit as st

st.set_page_config(page_title='Music', page_icon='🎹')
st.header("🎹 这才是真正的音乐 🎹")

music = [{
    'url': 'https://music.163.com/song/media/outer/url?id=2747536601.mp3',
    'photo': 'https://p2.music.126.net/pbhqhLU2ErvDZciRXW4oEQ==/109951172032139695.jpg?param=180y180',
    'name': '侧脸',
    'Author': '加木',
    'Lyrics': '''我只能察觉到她一半的爱
一半写在脸上 一半让我猜'''},
         {
    'url': 'https://music.163.com/song/media/outer/url?id=2749525442.mp3',
    'photo': 'https://p1.music.126.net/YbN2afAB9qu3BkzgKrnvnw==/109951172060884093.jpg?param=180y180',
    'name': '唤水剑',
    'Author': 'Sasioverlxrd',
    'Lyrics': '''我想在哪在哪我的唤水剑
今天见不到又不知道要等多少年'''},
         {
    'url': 'https://music.163.com/song/media/outer/url?id=2706786639.mp3',
    'photo': 'https://p1.music.126.net/eSoVpvVnsS6TCvDUWZWptQ==/109951171005786628.jpg?param=180y180',
    'name': '天下谁人不识君',
    'Author': '华云龙KLE',
    'Lyrics': '''她说不要担心家里 你该走走你的
我不知道她搁哪学会的说 你肯定能走起的'''},
         {
    'url': 'https://music.163.com/song/media/outer/url?id=2754174746.mp3',
    'photo': 'https://p2.music.126.net/niUkuo5bIZ3AbJ-BAYF3CQ==/109951172135987504.jpg?param=180y180',
    'name': '英雄',
    'Author': 'Asen',
    'Lyrics': '''我是他的心魔 给他留下疤痕
飞到世界各地就像Amazon'''},
         {
         'url': 'https://music.163.com/song/media/outer/url?id=1917411376.mp3',
    'photo': 'https://p2.music.126.net/cabX9QFRIZa2dHJny-qTpg==/109951167009569183.jpg?param=180y180',
    'name': '玛奇玛',
    'Author': 'Sasioverlxrd',
    'Lyrics': '''实在恨不起你这个精神控制者
这次说的喜欢你又要来通过谁'''}
         ]


if 'ind' not in st.session_state:
    st.session_state['ind'] = 0

def nextImg():
    st.session_state['ind'] = (st.session_state['ind'] + 1) % len(music)

def next2mg():
    st.session_state['ind'] = (st.session_state['ind'] - 1) % len(music)
    
d1, d2 = st.columns([1,2])

with d1:
    st.image(music[st.session_state['ind']]['photo'])

with d2:
    st.title(music[st.session_state['ind']]['name'])
    st.subheader(music[st.session_state['ind']]['Author'])
    st.text(music[st.session_state['ind']]['Lyrics'])

st.audio(music[st.session_state['ind']]['url'], autoplay=True)

c1, c2 = st.columns(2)
with c1:
    st.button('上一首', on_click=next2mg, use_container_width=True)

with c2:
    st.button('下一首', on_click=nextImg, use_container_width=True)
    
            
