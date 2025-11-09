# summarizer.py
import os
from dotenv import load_dotenv

# Ollama SDK
import ollama

# 读取 .env 配置
load_dotenv()
MODEL_NAME = os.getenv("OLLAMA_MODEL", "phi")  # 默认模型为 "phi"
MAX_TOKENS = int(os.getenv("OLLAMA_MAX_TOKENS", 16000))  # 改为 16000

def summarize_text(text: str) -> str:
    """
    使用 Ollama 本地模型生成 Markdown 学习笔记（英文）
    """
    if not text:
        return ""

    # 生成 prompt
    prompt = f"""
You are an educational assistant. Please summarize the following textbook content into **well-structured study notes** in **Markdown format**, using English only.

Requirements:
1. Preserve chapter titles and headings.
2. For each chapter, include:
   - **Definition**: Explain the concept briefly using bullet points.
   - **Key Points**: Use bullet points for main ideas.
   - **Examples**: Provide concrete examples if applicable.
3. Use proper Markdown syntax:
   - Chapters as '## Chapter Name'
   - Bullet points for definitions, examples, components, and important concepts.
4. Provide a **summary** at the end with main concepts in bullet points.
5. Keep the content concise but informative, covering all important points in the first {MAX_TOKENS} characters of text.

Text to summarize (first {MAX_TOKENS} characters):
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
        print(f"❌ Ollama failed to generate notes: {e}")
        return ""
