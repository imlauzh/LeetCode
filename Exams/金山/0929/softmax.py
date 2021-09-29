import numpy as np


def softmax(x):
    """
    对输入x的每一行计算softmax。
    该函数对于输入是向量（将向量视为单独的行）或者矩阵（M x N）均适用。
    代码利用softmax函数的性质: softmax(x) = softmax(x + c)
    参数:
    x -- 一个N维向量，或者M x N维numpy矩阵.
    返回值:
    x -- 在函数内部处理后的x
    """
    # 根据输入类型是矩阵还是向量分别计算softmax
    if len(x.shape) > 1:
        # 矩阵
        maxVal = np.max(x, axis=1)  # 得到每行的最大值，用于缩放每行的元素，避免溢出
        x -= maxVal.reshape((x.shape[0], 1))  # 利用性质缩放元素
        x = np.exp(x)  # 计算所有值的指数
        sumVal = np.sum(x, axis=1)  # 每行求和
        x /= sumVal.reshape((x.shape[0], 1))  # 求softmax
    else:
        # 向量
        maxVal = np.max(x)  # 得到最大值
        x -= maxVal  # 利用最大值缩放数据
        x = np.exp(x)  # 对所有元素求指数
        sumVal = np.sum(x)  # 求元素和
        x /= sumVal  # 求somftmax
    return x


test1 = np.array([1, 2, 3, 4])
print('原始向量:', test1)
print('经过softmax后:', softmax(test1))
