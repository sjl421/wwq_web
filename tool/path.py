import os


def one_level(source, offset):
    # 从当前source, 获得offset路径(offset和source相差一层目录)
    return os.path.join(os.path.dirname(source), offset)


def two_level(source, offset):
    # 从当前source, 获得offset路径(offset和source相差两层目录)
    return os.path.join(os.path.dirname(os.path.dirname(source)), offset)
