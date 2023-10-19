import streamlit as st
import brain
import random

home = False

def ayurbot():
    count = 0
    page_bg = """
    <style>
    [data-testid="stAppViewContainer"] {
    background-image: url("https://c4.wallpaperflare.com/wallpaper/586/603/742/minimalism-4k-for-mac-desktop-wallpaper-preview.jpg");
    background-size: cover;
    }        
    </style>
    """
    st.markdown(
        page_bg,
        unsafe_allow_html=True
    )
    st.markdown(
        """
        <h1 style="text-align: center; color: white; font-family: 'Times New Roman', Times, serif;">AYURBOT</h1>
        """,
        unsafe_allow_html=True
    )
    st.subheader('', divider='rainbow')
    st.markdown(
        """
        <h4 style="color: black;">Hi there! I am Chatbot specific to determine the Prakriti of an individual. So now lets determine your Prakriti!</h5>
        """,
        unsafe_allow_html=True
    )
    
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Send a message"):
        st.session_state.messages.append({"role":"USER","content": prompt})
        with st.chat_message("USER"):
            st.markdown(prompt)
            
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            bot_response=""
            prompt = prompt.lower()
            
            if prompt in brain.c_hi:
                bot_response = "Please answer the following questions honestly and accurately."

            if count==1 and prompt in brain.c_yes:
                bot_response = brain.questions(1)
            
            if count==2 and prompt in ans_1:
                bot_response = brain.questions(2)

            message_placeholder.markdown(bot_response)
        st.session_state.messages.append({"role": "assistant","content": bot_response})
        count+=1

def main():
    page_bg = """
    <style>
    [data-testid="stAppViewContainer"] {
    background-image: url("https://c4.wallpaperflare.com/wallpaper/586/603/742/minimalism-4k-for-mac-desktop-wallpaper-preview.jpg");
    background-size: cover;
    }        
    </style>
    """
    st.markdown(
        page_bg,
        unsafe_allow_html=True
    )
    st.markdown(
        """
        <h1 style="text-align: center; color: black; font-family: 'Times New Roman', Times, serif;">PRAKRITI</h1>
        """,
        unsafe_allow_html=True
    )
    st.subheader('', divider='rainbow')
    st.markdown(
        """
        <h5 style="color: black;">It is a term used in traditional Indian philosophy, particularly in Ayurveda, to describe the inherent constitution or nature of an individual.</h5>
        <h5 style="color: black;">In Ayurveda, it is believed that every person has a unique combination of three fundamental energies or doshas known as VATA, PITTA and KAPHA, which make up their Prakriti.</h5>
        <h5 style="color: black;">These doshas represent different combinationof five elements (Earth, Water, Fire, Air and Ether) and play physical and physcological characteristics as well as their susceptibility to certain health issues.</h5>
        
        """,
        unsafe_allow_html=True
    )
   
col1,col2,col3 = st.columns([1,1,5])
with col1:
    if st.button("HOME"):
        st.session_state.page = 'home'
with col2:
    if st.button("AYURBOT"):
        st.session_state.page = 'ayurbot'
    
if 'page' not in st.session_state:
    st.session_state.page = 'home'

if st.session_state.page == 'home':
    main()

if st.session_state.page == 'ayurbot':
    home = True
    ayurbot()