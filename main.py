import os
import openai
import streamlit as st
from langchain.chat_models import ChatOpenAI
import time

# from dotenv import load_dotenv, find_dotenv
# _ = load_dotenv(find_dotenv()) # read local .env file
openai.api_key = os.environ['OPENAI_API_KEY']

chat_model = ChatOpenAI()

st.title("인공지능 시인")

content = st.text_input('시의 주제를 제시해주세요.')

if st.button('시 작성 요청하기'):
    with st.spinner('시 작성 중...'):
        result = chat_model.predict(content + "에 대한 시를 써줘")
        st.write(result)
 
# result = chat_model.predict(content + "에 대한 시를 써줘")
# print(result)



# h1 태그의 span으로 들어감
# st.title("인공지능 시인")
# # st.title('_Streamlit is :blue[cool] :sunglasses:')  # 이모지

# # input 넣기
# title = st.text_input('시의 주제를 제시해주세요.')
# st.write('시의 주제는', title)


