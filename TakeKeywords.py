import openpyxl
import os
import subprocess


def read_xmp_with_exiftool(file_path):
    command = ['exiftool.exe', '-b', '-xmp:Subject', file_path]
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, text=True, check=True, encoding="UTF-8")
        xmp_data = ','.join(result.stdout.strip().split('\n'))  # 使用逗号分隔关键字
        return xmp_data
    except subprocess.CalledProcessError:
        print(f"Error reading XMP data for file: {file_path}")
        return ""


# 定义常量
FILE_NAME = 'Resource_Keywords.xlsx'
TITLE_ROW = ['文件夹名', '文件名', '关键词']

# 创建一个工作簿
workbook = openpyxl.Workbook()

# 获取默认的工作表
sheet = workbook.active

# 在第一行写入标题
sheet.append(TITLE_ROW)

dir_path = os.getcwd()

for dir_path, dir_names, file_names in os.walk(dir_path):
    for file_name in file_names:
        file_path = os.path.join(dir_path, file_name)
        keywords = read_xmp_with_exiftool(file_path)
        dir_name = os.path.basename(dir_path)
        sheet.append((dir_name, file_name, keywords))

# 保存工作簿到文件
workbook.save(FILE_NAME)
