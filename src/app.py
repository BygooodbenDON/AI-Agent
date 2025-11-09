# app.py
import sys
import os
import streamlit as st

# 把 src/ 加入模块搜索路径
sys.path.append(os.path.dirname(__file__))

from agents.pdf_reader import extract_text_from_file
from agents.summarizer import summarize_text
from utils.file_handler import save_output
from utils.text_cleaner import clean_text

# 页面标题
st.set_page_config(page_title="Auto Learning Assistant (Ollama)")

st.title("📚 Auto Learning Assistant (Ollama)")

uploaded_file = st.file_uploader(
    "Upload study material (PDF / DOCX / TXT)", type=["pdf", "docx", "txt"]
)

if uploaded_file:
    # 确保 input/output 文件夹存在
    os.makedirs("data/input", exist_ok=True)
    os.makedirs("data/output", exist_ok=True)

    input_path = f"data/input/{uploaded_file.name}"
    with open(input_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.write("⏳ Reading study material...")
    text = extract_text_from_file(input_path)

    st.write("⏳ Cleaning text...")
    text = clean_text(text)

    st.write("⏳ Generating study notes...")
    summary = summarize_text(text)

    if summary:
        # 保存输出
        save_output("data/output", uploaded_file.name, summary)
        st.success("✅ Notes generated successfully!")
        st.markdown(summary)
    else:
        st.error("❌ Failed to generate notes. Please check the model or content.")
