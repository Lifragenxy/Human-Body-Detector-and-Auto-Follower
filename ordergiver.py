import os
import xml.etree.ElementTree as ET


def get_type(file_path: str):
    for i in range(len(file_path))[::-1]:
        if file_path[i] == ".":
            return (i + 1) if (i + 1) < len(file_path) else -1

def get_ps(file_path: str, trg: str):
    for i in range(len(file_path))[::-1]:
        if file_path[i] == trg:
            return i


def traverse_files(folder_path, initial_order=0):
    """
    遍历一文件夹并批量给文件命名（切勿对同一文件夹使用2次！）
    :param folder_path: 被遍历的文件夹路径
    :param initial_order: 起始标号
    :return:
    """
    order = initial_order

    for root, dirs, files in os.walk(folder_path):

        for filename in files:

            file_path = os.path.join(root, filename)

            os.rename(file_path, file_path[:get_ps(file_path, "\\")] + "\\" + str(order) + "." +file_path[get_type(file_path):])

            order += 1

def order_fixer(folder_path):
    order = 0

    entries = os.listdir(folder_path)
    entries.sort(key=lambda a: int(a[:get_ps(a, ".")]))

    for file_name in entries:
        os.rename(folder_path + "\\" + file_name, folder_path + "\\" + str(order) + file_name[get_ps(file_name, "."):])

        order += 1

def xml_order_fixer(folder_path):
    order = 173

    entries = os.listdir(folder_path)
    entries.sort(key=lambda a: int(a[:get_ps(a, ".")]))

    for file_name in entries:
        if int(file_name[:get_ps(file_name, '.')]) >= order:
            tree = ET.parse(folder_path + "\\" + file_name)
            root = tree.getroot()
            for child in root:
                if child.tag == "filename":
                    child.text = str(order) + ".jpg"
                if child.tag == "path":
                    child.text = os.getcwd() + "\\" + folder_path + "\\" + file_name
            tree.write(folder_path + "\\" + file_name, encoding='utf-8', xml_declaration=True)
            order += 1

#traverse_files('datasets/ds1/JPEGImages')
#order_fixer('datasets/ds1/JPEGImages')
xml_order_fixer("dataset\\ds1\\annotation")