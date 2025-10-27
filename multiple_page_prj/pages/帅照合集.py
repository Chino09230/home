import streamlit as st

st.title("岸本跟踪C神画出来的Sasuke")

# 创建三个列容器，宽度比为3:1:2
col1, col2, col3 = st.columns(3)

# 使用点号语法
col1.subheader("帅")
col1.image('https://i.pinimg.com/originals/a8/b7/5d/a8b75db69b61724dd9a7ab134401a555.jpg?param180=180')

# 使用with语法
with col2:
    st.subheader("纯帅")
    st.image('https://gss0.baidu.com/-Po3dSag_xI4khGko9WTAnF6hhy/zhidao/pic/item/e4dde71190ef76c62ca8339c9e16fdfaaf51670b.jpg?param180=180')

# 使用with语法
with col3:
    st.subheader("硬帅")
    st.image('https://tse4.mm.bing.net/th/id/OIP.ngTOgV4xRU8q83C2BZQ0uAHaEo?rs=1&pid=ImgDetMain&o=7&rm=3https://c-ssl.duitang.com/uploads/blog/202008/12/20200812114309_wnwxu.jpeg?param180=180')
