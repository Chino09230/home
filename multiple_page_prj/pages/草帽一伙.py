import streamlit as st
import pandas as pd
import time


st.title(':blue[草帽一伙👒]')
st.markdown('## :yellow[🚢基本信息🚢]')
st.text('由“四皇”之一的蒙奇·D·路飞所创立的海贼团，旗帜图案是戴着草帽的骷髅')
st.markdown('''##### 当前进度:       *:green[艾格赫德]*       |       成员状态:*:green[全员完好]✅*
##### 任务目标:*:yellow[拯救贝加庞克]*    |任务进度:*:green[击败CP0]✅*''')

st.subheader('拯救贝加庞克')
progress_text_1 ="任务进行中，请稍等"
my_bar = st.progress(0,text=progress_text_1)
time.sleep(0.5)
for precent in range(80):
    time.sleep(0.1)
    my_bar.progress(precent+1,text=f'{progress_text_1},当前进度{precent}%:⌛:')

for precent in range(80,100):
    time.sleep(0.05)
    my_bar.progress(precent+1,text=f'即将完成任务,当前进度{precent}%:😄:')

st.subheader('团队关系⚯')
c1, c2, c3 = st.columns(3)
c1.metric(label="敌人", value="世界政府", delta="-BAD")
c2.metric(label="敌人", value="黑胡子海贼团", delta="-BAD")
c3.metric(label="同盟", value="心脏海贼团", delta="FRIEND")

data = {
    '草帽一伙':['蒙奇·D·路飞','罗罗诺亚·佐罗','娜美', '乌索普', '山治', '托尼托尼·乔巴','妮可·罗宾','弗兰奇','布鲁克','甚平'],
    '称号':['大船长·四皇·“草帽小子','海贼猎人','小贼猫','狙击之王','黑足','爱吃棉花糖的乔巴','恶魔之子','铁人·弗兰奇','灵魂之王','海侠·甚平']
}
index = pd.Series(['船长','战斗员', '航海士', '狙击手', '厨师', '船医','考古学家','船匠','音乐家','舵手'], name='职位')
df = pd.DataFrame(data, index=index)
st.subheader('成员🧑')
st.dataframe(df)

st.subheader('任务简介')
str = '''草帽一伙在航行过程中偶遇了乔艾莉·波妮，路飞为了救被风吹飞的乔巴和波妮而落入海中，
之后甚平将三人救下，并登陆了贝加班克的研究基地艾格赫德。路飞等人在岛上发现了200年前曾袭击玛丽乔亚
的古代机器人，并与贝加班克相识。因为贝加庞克涉嫌研究空白的一百年成为了世界政府的抹杀对象，
于是他希望路飞等人能够带他离开艾格赫德。路飞认为贝加庞克很有趣，于是答应了他的请求。
而这时CP0抵达了艾格赫德，路飞与罗布·路奇再次展开了对战，路奇被五档形态下的路飞全程压制，
最终在路飞的攻击下失去了意识。
'''
st.code(str, language=None)

st.markdown('***')
st.markdown('###### :green[Next Message:]击败世界政府')
st.markdown('###### :green[Target:]寻找OnePiece!')
st.markdown('###### :green[Countdown:]25-10-20')

st.text('系统状态:在线  连接状态:已加密')
