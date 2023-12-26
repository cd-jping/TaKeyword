

import subprocess
import json

def extract_xmp_info(file_path):
    try:
        # 使用exiftool执行命令获取JSON格式的元数据
        result = subprocess.run(['exiftool', '-XMP', '-b', '-json', file_path], capture_output=True, text=True)
        if result.returncode == 0:
            xmp_data = json.loads(result.stdout)
            return xmp_data[0]['XMP']
        else:
            print(f"Error extracting XMP information from {file_path}: {result.stderr}")
            return None
    except Exception as e:
        print(f"Error extracting XMP information from {file_path}: {e}")
        return None




# 示例用法
file_path = "TestDir/CatDir2/礼物.png"
xmp_data = extract_xmp_info(file_path)  # 假设这是获取的XMP数据


# 如果ture
if is_valid_xml(xmp_data):
    print("XMP data is valid XML.")
else:
    print("XMP data is not valid XML.")

import subprocess
import xml.etree.ElementTree as ET
import json


def extract_subject_li_content(xmp_data):
    try:
        subject_li_content = []

        # 查找所有 <dc:subject> 标签
        print("a")
        print(xmp_data)
        xmp_xml = ET.fromstring(xmp_data)
        subjects = xmp_xml.findall(".//{http://purl.org/dc/elements/1.1/}subject")
        print("B")
        # 遍历每个 <dc:subject> 标签
        for subject in subjects:
            # 查找该标签下的所有 <li> 标签
            li_elements = subject.findall(".//{http://www.w3.org/1999/02/22-rdf-syntax-ns#}li")

            # 提取每个 <li> 标签的内容
            li_content = [li.text for li in li_elements if li.text]
            # 将结果添加到列表中
            subject_li_content = li_content

        return subject_li_content
    except Exception as e:
        print(f"Error extracting subject li content: {e}")
        return None


# 示例用法

if xmp_data:
    subject_li_content = extract_subject_li_content(xmp_data)

    if subject_li_content:
        print(f"Content of <dc:subject><li>: {subject_li_content}")
    else:
        print("No <dc:subject><li> content found.")

