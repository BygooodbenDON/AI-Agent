# main.py
import os
from agents.pdf_reader import extract_text_from_file
from agents.summarizer import summarize_text
from utils.file_handler import save_output
from dotenv import load_dotenv

# 加载 .env 配置（可选）
load_dotenv()

# 输入输出目录（可从 .env 或固定）
INPUT_DIR = os.getenv("INPUT_DIR", "data/input")
OUTPUT_DIR = os.getenv("OUTPUT_DIR", "data/output")

def main():
    # 确保输出文件夹存在
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # 遍历 input 文件夹
    for file_name in os.listdir(INPUT_DIR):
        if not file_name.lower().endswith((".pdf", ".docx", ".txt")):
            continue

        file_path = os.path.join(INPUT_DIR, file_name)
        print(f"📄 正在处理: {file_name}")

        # 1️⃣ 读取文件文本
        text = extract_text_from_file(file_path)
        if not text:
            print(f"⚠️ 未提取到文本: {file_name}")
            continue

        # 2️⃣ 调用 Ollama 生成学习笔记
        summary = summarize_text(text)

        # 3️⃣ 保存输出文件
        save_output(OUTPUT_DIR, file_name, summary)

if __name__ == "__main__":
    main()
