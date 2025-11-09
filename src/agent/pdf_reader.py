import pdfplumber
import docx
import os

def extract_text_from_pdf(file_path):
    """读取 PDF 文件内容，返回纯文本"""
    text = ""
    try:
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
    except Exception as e:
        print(f"❌ PDF 读取失败: {file_path}, {e}")
    return text

def extract_text_from_docx(file_path):
    """读取 DOCX 文件内容，返回纯文本"""
    text = ""
    try:
        doc = docx.Document(file_path)
        for para in doc.paragraphs:
            text += para.text + "\n"
    except Exception as e:
        print(f"❌ DOCX 读取失败: {file_path}, {e}")
    return text

def extract_text_from_txt(file_path):
    """读取 TXT 文件内容，返回纯文本"""
    text = ""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()
    except Exception as e:
        print(f"❌ TXT 读取失败: {file_path}, {e}")
    return text

def extract_text_from_file(file_path):
    """根据文件类型自动选择解析方法"""
    ext = os.path.splitext(file_path)[1].lower()
    if ext == ".pdf":
        return extract_text_from_pdf(file_path)
    elif ext == ".docx":
        return extract_text_from_docx(file_path)
    elif ext == ".txt":
        return extract_text_from_txt(file_path)
    else:
        print(f"⚠️ 不支持的文件格式: {file_path}")
        return ""
