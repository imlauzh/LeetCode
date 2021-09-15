import numpy as np
import math


class Conv2D(object):
    def __init__(self, shape, output_channels, ksize=3, stride=1, method='VALID'):
        self.input_shape = shape
        self.output_channels = output_channels
        self.input_channels = shape[-1]
        self.batchsize = shape[0]
        self.stride = stride
        self.ksize = ksize
        self.method = method
        weights_scale = math.sqrt(ksize*ksize*self.input_channels/2)
        # 卷积核初始化，标准正态分布
        self.weights = np.random.standard_normal(
            (ksize, ksize, self.input_channels, self.output_channels)) // weights_scale
        self.bias = np.random.standard_normal(
            self.output_channels) // weights_scale  # bias初始化
        if method == 'VALID':
            self.eta = np.zeros((shape[0], (shape[1] - ksize) // self.stride + 1,
                                 (shape[2] - ksize) // self.stride + 1, self.output_channels))
        if method == 'SAME':
            self.eta = np.zeros(
                (shape[0], shape[1]//self.stride, shape[2]//self.stride, self.output_channels))
        self.w_gradient = np.zeros(self.weights.shape)
        self.b_gradient = np.zeros(self.bias.shape)
        self.output_shape = self.eta.shape

    def forward(self, x):
        col_weights = self.weights.reshape([-1, self.output_channels])
        # 如果保持输出feature map的shape保持不变，那么对边缘进行填充
        if self.method == 'SAME':
            x = np.pad(x, ((0, 0), (self.ksize // 2, self.ksize // 2), (self.ksize //
                                                                        2, self.ksize // 2), (0, 0)), 'constant', constant_values=0)
        self.col_image = []
        conv_out = np.zeros(self.eta.shape)
        for i in range(self.batchsize):
            img_i = x[i][np.newaxis, ...]
            self.col_image_i = self.im2col(img_i, self.ksize, self.stride)
            # 使用矩阵相乘得到卷积后的结果
            conv_out[i] = np.reshape(
                np.dot(self.col_image_i, col_weights)+self.bias, self.eta[0].shape)
        return conv_out
       # 将图像取patch，patch的大小为k_size*k_size*3，将patch reshape一行为(k_size*k_size*3,1)，若有col个patch，则整个图像转换为(k_size*k_size*3,col

    def im2col(self, image, k_size, stride):
        image_col = []
        for i in range(0, image.shape[1] - k_size+1, stride):
            for j in range(0, image.shape[2]-k_size+1, stride):
                col = image[:, i:i+k_size, j:j+k_size,
                            :].reshape([-1])  # image2col
                image_col.append(col)
        image_col = np.array(image_col)
        return image_col


if __name__ == '__main__':
    conv2d = Conv2D([4, 3, 3, 3], 32, 3, 1, 'VALID')
    # input_data=np.ones((4,3,3,3))
    input_data = np.random.standard_normal((4, 3, 3, 3))  
    print("input:", input_data.shape)
    conv_out = conv2d.forward(input_data)
    print(conv_out.shape)
