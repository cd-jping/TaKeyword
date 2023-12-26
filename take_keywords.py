import openpyxl
import os
import subprocess


def read_xmp_with_exiftool(file_path):
    command = ['exiftool', '-b', '-xmp:Subject', file_path]
    result = subprocess.run(command, stdout=subprocess.PIPE, text=True)
    xmp_data = ','.join(result.stdout.strip().split('\n'))  # 使用逗号分隔关键字
    return xmp_data


# 创建一个工作簿
workbook = openpyxl.Workbook()

# 获取默认的工作表
sheet = workbook.active

# 在第一行写入标题
sheet['A1'] = '文件夹名'
sheet['B1'] = '文件名'
sheet['C1'] = '关键词'

dir_path = os.getcwd()
for dir_path, dir_names, file_names in os.walk(dir_path):

    for file_name in file_names:
        keywords = read_xmp_with_exiftool(os.path.join(dir_path, file_name))
        dir_name = os.path.basename(dir_path)
        sheet.append([dir_name, file_name, keywords])

# 保存工作簿到文件
workbook.save('Resource_Keywords.xlsx')
