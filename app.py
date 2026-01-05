from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

st.title("ダイエット相談アプリ")
st.write("##### フードコーディネーター")
st.write("入力フォームにフードコーディネーターに相談したいテキストを入力し、「聞いてみる」ボタンを押すことでフードコーディネーターからのアドバイスを得られます。")
st.write("##### フィットネスアドバイザー")
st.write("入力フォームにフィットネスアドバイザーに相談したいテキストを入力し、「聞いてみる」ボタンを押すことでフィットネスアドバイザーからのアドバイスを得られます。")

selected_item = st.radio(
    "どちらに相談しますか？。",
    ["フードコーディネーター", "フィットネスアドバイザー"]
)

st.divider()

if selected_item == "フードコーディネーター":
    input_message = st.text_input(label="私はフードコーディネーターです。何かお困りですか？")

else:
    input_message = st.text_input(label="私はフィットネスアドバイザーです。何かお困りですか？")

if st.button("聞いてみる"):
    st.divider()

    if selected_item == "フードコーディネーター":
        system_promot="あなたは経験豊富なフードコーディネーターです。ユーザーからの相談に対して、食事についてのアドバイスを中心に、親切かつ具体的なアドバイスを提供してください。"
    else:
        system_promot="あなたは経験豊富なフィットネスアドバイザーです。ユーザーからの相談に対して、運動についてのアドバイスを中心に、親切かつ具体的なアドバイスを提供してください。"
    
    if input_message:
            messages = [
            SystemMessage(content=system_promot),
            HumanMessage(content=input_message),
            ]
            result = llm(messages)
            st.write(result.content)
    else:
            st.error("相談したいことを入力してから「聞いてみる」ボタンを押してください。")
