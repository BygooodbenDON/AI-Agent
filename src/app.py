# app.py
import streamlit as st
import os
from agents.pdf_reader import extract_text_from_file
from agents.summarizer import summarize_text
from utils.file_handler import save_output
from utils.text_cleaner import clean_text

# 页面标题
st.set_page_config(page_title="Auto Learning Assistant (Ollama)")

st.title("📚 Auto Learning Assistant (Ollama)")

uploaded_file = st.file_uploader(
    "上传教材文件（PDF / DOCX / TXT）", type=["pdf", "docx", "txt"]
)

if uploaded_file:
    # 确保 input/output 文件夹存在
    os.makedirs("data/input", exist_ok=True)
    os.makedirs("data/output", exist_ok=True)

    input_path = f"data/input/{uploaded_file.name}"
    with open(input_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.write("⏳ 正在读取教材...")
    text = extract_text_from_file(input_path)

    st.write("⏳ 正在清理文本...")
    text = clean_text(text)

    st.write("⏳ 正在生成笔记...")
    summary = summarize_text(text)

    # 保存输出
    save_output("data/output", uploaded_file.name, summary)

    st.success("✅ 生成完成！")
    st.markdown(summary)
