import streamlit as st
import os
os.environ["OPENAI_API_KEY"] = "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"
import pandas as pd
from llama_index.experimental.query_engine import PandasQueryEngine

USER_NAME = "USER"
ASSISTANT_NAME = "AI"

st.markdown('### 山田はなこ 田中あい 佐藤さき、について質問ができます。')
st.markdown('質問の種類：年齢、バスト、3サイズ、プレー、コース、出勤中、出勤曜日、おすすめ、英語可能か、好きなプレイ、おすすめ')

df = pd.DataFrame(
  data = {
      "girl name": ["山田はなこ", "田中あい", "佐藤さき"],
      "age" :  [23, 21, 25],
      "bust" :  ["80cm", "90cm", "100cm"],
      "cup" :  ["C cup", "E cup", "H cup"],
      "height": [160, 170, 180],
      "hip": ["82cm", "88cm", "95cm"],
      "waist": ["42cm", "48cm", "45cm"],
      "available plays": [
            ["anal", "blowjob", "vibration", "3p", "squirting"],
            ["anal", "bondage", "vibration", "3p", "cumshot"],
            ["blowjob", "bondage", "vibration", "3p", "titsfuck"],
      ],
      "currently working": ["no", "yes", "no"],
      "english": ["yes", "no", "no"],
      "course": [
            ["VIP S", "VIP PREMIUM PERL", "IMAGE S"],
            ["VIP PREMIUM RUBY", "IMAGE S"],
            ["VIP S", "VIP PREMIUM SAPPHIRE"],
      ],
      "favorite play": ["3p", "bondage", "titsfuck"],
      "work schedule": [
          ["monday", "tuesday", "wednesday"],
          ["thursday", "saturday", "sunday", "friday"],
          ["wednesday", "thursday", "friday"],
      ],
      "recommended": ["yes", "no", "no"],
      "shop": ["shinuku", "ikebukuro", "gotanda"]
      }
)

query_engine = PandasQueryEngine(df=df, verbose=True, synthesize_response=True)

if "chat_log" not in st.session_state:
    st.session_state.chat_log = []

# 質問の入力
question = st.chat_input('質問を入力してください')

if question:

    for chat in st.session_state.chat_log:
        with st.chat_message(chat["name"], avatar=chat["avatar"]):
            st.write(chat["msg"])

    response = query_engine.query(question)

    with st.chat_message(USER_NAME, avatar="😃"):
        st.write(question)

    with st.chat_message(ASSISTANT_NAME, avatar="👩🏻"):
        st.write(response.response)

    #message = st.chat_message("assistant")
    #message.write(response.response)

    st.session_state.chat_log.append({"name": USER_NAME, "msg": question, "avatar": "😃"})
    st.session_state.chat_log.append({"name": ASSISTANT_NAME, "msg": response.response, "avatar": "👩🏻‍💼"})
