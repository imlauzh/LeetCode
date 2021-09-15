import torch
import torch.nn as nn
import numpy as np
import math


class LayerNorm(nn.Module):
    def __init__(self,
                 dimension: int,
                 eps: float = 1e-6
                 ) -> None:
        super().__init__()
        self.gamma = nn.Parameter(torch.ones(dimension))
        self.beta = nn.Parameter(torch.zeros(dimension))
        self.eps = eps

    def forward(self, tensor: torch.Tensor):  # pylint: disable=arguments-differ
        # 注意，是针对最后一个维度进行求解~
        mean = tensor.mean(-1, keepdim=True)
        std = tensor.std(-1, unbiased=False, keepdim=True)
        return self.gamma * (tensor - mean) / (std + self.eps) + self.beta


class SelfAttention(nn.Module):
    def __init__(self, input_size, hidden_size, attention_dropout_prob, hidden_dropout_prob):
        super(SelfAttention, self).__init__()

        self.input_size = input_size
        self.hidden_size = hidden_size

        # Wq Wk Wv参数矩阵，尺寸为[H, H](768, 768)
        self.query = nn.Linear(input_size, self.hidden_size)
        self.key = nn.Linear(input_size, self.hidden_size)
        self.value = nn.Linear(input_size, self.hidden_size)

        self.attn_dropout = nn.Dropout(attention_dropout_prob)

        # 做完self-attention 做一个前馈全连接 LayerNorm 输出
        self.dense = nn.Linear(hidden_size, hidden_size)
        self.LayerNorm = LayerNorm(hidden_size)
        self.out_dropout = nn.Dropout(hidden_dropout_prob)

    # 前向传播函数，输入尺寸：[B, S, H](32, 128, 768)， 输出尺寸：[B, S, H](32, 128, 768)

    def forward(self, input_tensor):

        # Q K V 矩阵 尺寸为[B, S, H](32, 128, 768)
        query_layer = self.query(input_tensor)
        key_layer = self.key(input_tensor)
        value_layer = self.value(input_tensor)

        # 将"query"和"key"点乘，得到未经处理注意力值
        # attention_scores 尺寸为[B, S, S](32, 128, 128)
        # 两个三维向量相乘，(B*S*H)*(B*H*S)=B*S*S
        attention_scores = torch.matmul(query_layer, key_layer.transpose(1, 2))

        # 标准化，避免内积过大 1/sqrt(d_k)
        attention_scores = attention_scores / math.sqrt(self.input_size)

        # 使用 softmax 函数将注意力值标准化成概率值
        attention_probs = nn.Softmax(dim=-1)(attention_scores)
        # dropout
        attention_probs = self.attn_dropout(attention_probs)
        # context_layer = softmax(Q * K^T) * V
        # 尺寸为[B, S, H], (32, 128, 768)
        context_layer = torch.matmul(attention_probs, value_layer)

        return context_layer

    def forward_with_mask(self, input_tensor, attention_mask):
        # batch*1*1*seqlen 增加维度
        attention_mask = attention_mask.unsqueeze(1).unsqueeze(2)
        # padding 的 token置为负无穷
        attention_mask = (1.0 - attention_mask) * (-np.Inf)

        # Q K V 矩阵 尺寸为[B, S, H](32, 128, 768)
        query_layer = self.query(input_tensor)
        key_layer = self.key(input_tensor)
        value_layer = self.value(input_tensor)

        # 将"query"和"key"点乘，得到未经处理注意力值
        # attention_scores 尺寸为[B, S, S](32, 128, 128)
        # 两个三维向量相乘，(B*S*H)*(B*H*S)=B*S*S
        attention_scores = torch.matmul(query_layer, key_layer.transpose(1, 2))

        # 标准化，避免内积过大 1/sqrt(d_k)
        attention_scores = attention_scores / math.sqrt(self.input_size)

        # [batch_size 1 1 seq_len]
        attention_scores = attention_scores + attention_mask

        # 使用 softmax 函数将注意力值标准化成概率值
        attention_probs = nn.Softmax(dim=-1)(attention_scores)
        # dropout
        attention_probs = self.attn_dropout(attention_probs)
        # context_layer = softmax(Q * K^T) * V
        # 尺寸为[B, S, H], (32, 128, 768)
        context_layer = torch.matmul(attention_probs, value_layer)

        return context_layer
