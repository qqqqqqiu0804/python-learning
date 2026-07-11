"""测试文件"""
import pytest
from pathlib import Path
from utils import get_file_list, preview_rename

def test_get_file_list(tmp_path):
    """测试获取文件列表"""
    # 创建测试文件
    (tmp_path / "file1.txt").touch()
    (tmp_path / "file2.txt").touch()
    (tmp_path / "image.jpg").touch()
    
    # 测试获取所有文件
    files = get_file_list(tmp_path)
    assert len(files) == 3
    
    # 测试按扩展名过滤
    txt_files = get_file_list(tmp_path, ".txt")
    assert len(txt_files) == 2

def test_preview_rename(capsys):
    """测试预览重命名"""
    original = ["file1.txt", "file2.txt"]
    new = ["001.txt", "002.txt"]
    
    preview_rename(original, new)
    captured = capsys.readouterr()
    assert "file1.txt -> 001.txt" in captured.out
    assert "共 2 个文件" in captured.out