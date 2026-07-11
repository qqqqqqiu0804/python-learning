"""工具函数模块"""
import os
from pathlib import Path
from datetime import datetime

def get_file_list(directory, extension=None):
    """获取文件列表"""
    path = Path(directory)
    if not path.exists():
        raise FileNotFoundError(f"目录不存在: {directory}")
    
    files = []
    for item in path.iterdir():
        if item.is_file():
            if extension is None or item.suffix.lower() == extension.lower():
                files.append(item)
    return sorted(files)

def preview_rename(original_names, new_names):
    """预览重命名效果"""
    print("\n预览重命名效果:")
    print("-" * 50)
    for old, new in zip(original_names, new_names):
        print(f"{old} -> {new}")
    print("-" * 50)
    print(f"共 {len(new_names)} 个文件")

def confirm_rename():
    """确认重命名操作"""
    response = input("确认执行重命名? (y/N): ").strip().lower()
    return response in ('y', 'yes', '是')
