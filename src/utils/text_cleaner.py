# text_cleaner.py
import re

def clean_text(text: str) -> str:
    """
    清理文本：
    - 去掉多余空行
    - 去掉连续空格
    - 移除控制字符（如 \x0c）
    """
    if not text:
        return ""

    # 移除控制字符
    text = re.sub(r"[\x00-\x1f\x7f]", "", text)

    # 替换多个空格为一个空格
    text = re.sub(r"[ \t]+", " ", text)

    # 替换多个换行符为一个换行
    text = re.sub(r"\n\s*\n+", "\n\n", text)

    # 去掉首尾空格
    text = text.strip()

    return text
