"""文件批量重命名工具"""
import os
import click
from pathlib import Path
from datetime import datetime
from utils import get_file_list, preview_rename, confirm_rename

@click.group()
def cli():
    """文件批量重命名工具"""
    pass

@cli.command()
@click.argument('directory')
@click.option('--start', default=1, help='起始序号')
@click.option('--prefix', default='', help='前缀')
@click.option('--suffix', default='', help='后缀')
def by_sequence(directory, start, prefix, suffix):
    """按序号重命名文件"""
    files = get_file_list(directory)
    if not files:
        print("没有找到文件")
        return
    
    original_names = []
    new_names = []
    
    for i, file in enumerate(files, start=start):
        original_names.append(file.name)
        new_name = f"{prefix}{i:03d}{suffix}{file.suffix}"
        new_names.append(new_name)
    
    preview_rename(original_names, new_names)
    
    if confirm_rename():
        for file, new_name in zip(files, new_names):
            new_path = file.parent / new_name
            file.rename(new_path)
        print("重命名完成!")
    else:
        print("已取消重命名")

@cli.command()
@click.argument('directory')
@click.option('--old', required=True, help='要替换的文本')
@click.option('--new', required=True, help='替换后的文本')
def replace(directory, old, new):
    """查找替换重命名文件"""
    files = get_file_list(directory)
    if not files:
        print("没有找到文件")
        return
    
    original_names = []
    new_names = []
    
    for file in files:
        original_names.append(file.name)
        new_name = file.name.replace(old, new)
        new_names.append(new_name)
    
    preview_rename(original_names, new_names)
    
    if confirm_rename():
        for file, new_name in zip(files, new_names):
            new_path = file.parent / new_name
            file.rename(new_path)
        print("重命名完成!")
    else:
        print("已取消重命名")

if __name__ == '__main__':
    cli()
