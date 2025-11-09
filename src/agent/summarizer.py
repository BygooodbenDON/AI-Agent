# summarizer.py
import os
from dotenv import load_dotenv

# Ollama SDK
import ollama

# 读取 .env 配置（可选）
load_dotenv()
MODEL_NAME = os.getenv("OLLAMA_MODEL", "mistral")  # 默认模型为 "mistral"
MAX_TOKENS = int(os.getenv("OLLAMA_MAX_TOKENS", 4000))

def summarize_text(text: str) -> str:
    """
    使用 Ollama 本地模型生成 Markdown 学习笔记
    """
    if not text:
        return ""

    # 生成 prompt
    prompt = f"""
请将以下内容整理成有条理的学习笔记，保留章节和关键点，并输出 Markdown 格式：
{text[:MAX_TOKENS]}
"""

    try:
        response = ollama.chat(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": prompt}],
        )
        # Ollama 返回的文本
        summary = response['message']['content']
        return summary
    except Exception as e:
        print(f"❌ Ollama 生成笔记失败: {e}")
        return ""
