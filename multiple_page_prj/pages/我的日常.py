import streamlit as st

st.set_page_config(page_title='Delta Force', page_icon='🔺')
st.header("🤘🏽 我的日常 🤘")

video = [{
    'url':'https://upos-sz-mirrorcosov.bilivideo.com/upgcxcode/42/66/33133756642/33133756642-1-192.mp4?e=ig8euxZM2rNcNbNMhwdVhwdlhbKVhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&os=cosovbv&og=hw&deadline=1761301871&oi=771356656&trid=8f49d0b76df541369347ee2c8ea700ah&nbs=1&uipk=5&platform=html5&mid=0&gen=playurlv3&upsig=f55101c13eec69d98026bb46939cf72a&uparams=e,os,og,deadline,oi,trid,nbs,uipk,platform,mid,gen&bvc=vod&nettype=0&bw=1924611&agrr=1&buvid=&build=0&dl=0&f=h_0_0&orderid=0,1',
    'title':'只玩帅的',
    'episode':'1',
    'Author': '👤 YLG小叶',
    'Map':'🗺 巴克什',
    'k':'小帅'
    },
              {
    'url':'https://upos-sz-mirrorcosov.bilivideo.com/upgcxcode/44/06/30609900644/30609900644-1-192.mp4?e=ig8euxZM2rNcNbNMhWdVhwdlhbK1hwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&oi=771356656&gen=playurlv3&og=ali&nbs=1&mid=0&deadline=1761301983&os=cosovbv&uipk=5&platform=html5&trid=d96cb9aae9a04e39b3bdadbada702aeh&upsig=caa297eca5a110d16641b2d5f3dba5ab&uparams=e,oi,gen,og,nbs,mid,deadline,os,uipk,platform,trid&bvc=vod&nettype=0&bw=1939574&build=0&dl=0&f=h_0_0&agrr=1&buvid=&orderid=0,1',
    'title':'只玩帅的',
    'episode':'2',
    'Author': '👤 丷Bling',
    'Map':'🗺 航天基地\巴克什',
    'k':'中帅'},
              {
    'url':'https://upos-sz-mirrorcosov.bilivideo.com/upgcxcode/59/90/31978229059/31978229059_qe1-1-192.mp4?e=ig8euxZM2rNcNbNzhbdVhwdlhbhghwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&trid=ca792c4a54e347f48eb111a9ef31b0bh&uipk=5&platform=html5&gen=playurlv3&os=cosovbv&og=cos&oi=771356656&mid=0&nbs=1&deadline=1761302036&upsig=944232e953a3265b3c742952928d84e4&uparams=e,trid,uipk,platform,gen,os,og,oi,mid,nbs,deadline&bvc=vod&nettype=0&bw=1866255&f=h_0_0&agrr=1&buvid=&build=0&dl=0&orderid=0,1',
    'title':'只玩帅的',
    'episode':'3',
    'Author': '👤 苏6の',
    'Map':'🗺 航天基地\潮汐监狱',
    'k':'大帅'},
         {
    'url':'https://upos-sz-mirrorcosov.bilivideo.com/upgcxcode/65/91/32904709165/32904709165-1-192.mp4?e=ig8euxZM2rNcNbNM7zdVhwdlhbKahwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&platform=html5&mid=0&deadline=1761302314&uipk=5&gen=playurlv3&og=cos&nbs=1&oi=771356656&trid=378bd57889fb4c5eb2ad0c5a9001a75h&os=cosovbv&upsig=49ffce4cd47d21514acfa0ebb5698fac&uparams=e,platform,mid,deadline,uipk,gen,og,nbs,oi,trid,os&bvc=vod&nettype=0&bw=1992653&build=0&dl=0&f=h_0_0&agrr=1&buvid=&orderid=0,1',
    'title':'只玩帅的',
    'episode':'4',
    'Author': '👤 璃茉Kira',
    'Map':'🗺 航天基地',
    'k':'超帅'}
         ]

if 'ind' not in st.session_state:
    st.session_state['ind'] = 0
    

st.title(video[st.session_state['ind']]['title'] + '-第' + video[st.session_state['ind']]['episode'] + '集')

st.header(video[st.session_state['ind']]['k'])

st.subheader(video[st.session_state['ind']]['Author'] + video[st.session_state['ind']]['Map'])


st.video(video[st.session_state['ind']]['url'])

def play(arg):
    st.session_state['ind'] = int(arg)
   
for x in range(len(video)):
    st.button('第' + str(x+1) + '集', use_container_width=True, on_click=play, args=([x]))

