# file_handler.py
import os

def save_output(output_dir: str, input_file_name: str, content: str):
    """
    保存生成的笔记到 output 文件夹
    自动加上 '_summary.md' 后缀
    """
    if not content:
        print(f"⚠️ 内容为空，未保存: {input_file_name}")
        return

    os.makedirs(output_dir, exist_ok=True)
    base_name = os.path.splitext(input_file_name)[0]
    output_file = os.path.join(output_dir, f"{base_name}_summary.md")

    try:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"✅ 已保存: {output_file}")
    except Exception as e:
        print(f"❌ 保存失败: {output_file}, {e}")
