import os


def get_type(file_path: str):
    for i in range(len(file_path))[::-1]:
        if file_path[i] == ".":
            return (i + 1) if (i + 1) < len(file_path) else -1

def get_ps(file_path: str, trg: str):
    for i in range(len(file_path))[::-1]:
        if file_path[i] == trg:
            return i


def traverse_files(folder_path):
    order = 0

    for root, dirs, files in os.walk(folder_path):

        for filename in files:

            file_path = os.path.join(root, filename)

            os.rename(file_path, file_path[:get_ps(file_path, "\\")] + "\\" + str(order) + "." +file_path[get_type(file_path):])

            order += 1

traverse_files('dataset/ds1/annotation')