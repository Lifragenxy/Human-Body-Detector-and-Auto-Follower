import os
import random


def main():
    random.seed(0)  # 设置随机种子，保证随机结果可复现

    # 给定数据集Annotation的路径
    files_path = "./VOCdevkit/VOC2012/Annotations"
    assert os.path.exists(files_path), "path: '{}' does not exist.".format(files_path)

    # 验证集的比例
    val_rate = 0.2  # 因为测试集不公开，训练：验证集=8:2

    """
        for file in os.listdir(files_path)
            其中os.listdir(files_path)遍历该路径下所有的文件
            file就是一个一个文件
        file.split(".")[0]
            分割字符串并取出文件名
        sorted()
            排序函数
        Note: 列表表达式最后得到肯定是一个list
    """
    files_name = sorted([file.split(".")[0] for file in os.listdir(files_path)])
    files_num = len(files_name)  # 得到文件的数量

    """
        random.sample(序列，k=采样个数)
            可以简单理解为从某个list中随机采样k个点（且k不会重复）
            返回值是一个list
                >>> import random
                >>> random.sample(range(0, 10), 6)
                [8, 3, 7, 0, 6, 2]

        random.sample(range(0, files_num), k=int(files_num*val_rate))
            从0到files_num-1中随机采样files_num*val_rate个点组成一个list并返回
    """
    val_index = random.sample(range(0, files_num), k=int(files_num * val_rate))
    train_files = []
    val_files = []

    # files_name是一个list，list可以被enumerate
    for index, file_name in enumerate(files_name):
        if index in val_index:  # 如果这张图片是采样图片，则放入验证集
            val_files.append(file_name)
        else:
            train_files.append(file_name)  # 否则放入训练集

    try:
        # 'x'用于创建并写入新文件
        # \n 表示换行符
        train_f = open("train.txt", "x")
        eval_f = open("val.txt", "x")
        train_f.write("\n".join(train_files))
        eval_f.write("\n".join(val_files))
    except FileExistsError as e:
        print(e)
        exit(1)


if __name__ == '__main__':
    main()