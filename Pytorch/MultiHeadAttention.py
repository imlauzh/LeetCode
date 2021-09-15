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


class MultiHeadAttention(nn.Module):
    def __init__(self, num_attention_heads, input_size, hidden_size, attention_dropout_prob, hidden_dropout_prob):
        super(MultiHeadAttention, self).__init__()
        if hidden_size % num_attention_heads != 0:
            raise ValueError(
                "The hidden size (%d) is not a multiple of the number of attention "
                "heads (%d)" % (hidden_size, num_attention_heads))
        self.num_attention_heads = num_attention_heads
        self.attention_head_size = int(hidden_size / num_attention_heads)
        self.all_head_size = hidden_size

        # Wq Wk Wv参数矩阵，尺寸为[H, H](768, 768)
        self.query = nn.Linear(input_size, self.all_head_size)
        self.key = nn.Linear(input_size, self.all_head_size)
        self.value = nn.Linear(input_size, self.all_head_size)

        self.attn_dropout = nn.Dropout(attention_dropout_prob)

        # 做完self-attention 做一个前馈全连接 LayerNorm 输出
        self.dense = nn.Linear(hidden_size, hidden_size)
        self.LayerNorm = LayerNorm(hidden_size)
        self.out_dropout = nn.Dropout(hidden_dropout_prob)

    # 维度转换函数，输入尺寸：[B, S, H](32, 128, 768)， 输出尺寸：[B, N, S, H/N](32, 8, 128, 768/8)
    def transpose_for_scores(self, x):
        # new_x_shape = [B, S, N, H/N](32, 128, 8, 768/8)
        new_x_shape = x.size()[
            :-1] + (self.num_attention_heads, self.attention_head_size)
        x = x.view(*new_x_shape)
        # x.shape = [B, N, S, H/N](32, 8, 128, 768/8)
        return x.permute(0, 2, 1, 3)

    # 前向传播函数，输入尺寸：[B, S, H](32, 128, 768)， 输出尺寸：[B, S, H](32, 128, 768)
    def forward(self, input_tensor):

        # Q K V 矩阵 尺寸为[B, S, H](32, 128, 768)
        mixed_query_layer = self.query(input_tensor)
        mixed_key_layer = self.key(input_tensor)
        mixed_value_layer = self.value(input_tensor)

        # 转置后Q K V 矩阵尺寸为[B, N, S, H/N](32, 8, 128, 768/8)
        query_layer = self.transpose_for_scores(mixed_query_layer)
        key_layer = self.transpose_for_scores(mixed_key_layer)
        value_layer = self.transpose_for_scores(mixed_value_layer)

        # 将"query"和"key"点乘，得到未经处理注意力值
        # attention_scores 尺寸为[B, N, S, S](32, 8, 128, 128)
        # Take the dot product between "query" and "key" to get the raw attention scores.
        attention_scores = torch.matmul(
            query_layer, key_layer.transpose(-1, -2))

        # 标准化，避免内积过大 1/sqrt(d_k)
        attention_scores = attention_scores / \
            math.sqrt(self.attention_head_size)
        # Apply the attention mask is (precomputed for all layers in BertModel forward() function)
        # [batch_size heads seq_len seq_len] scores
        # [batch_size 1 1 seq_len]

        # attention_scores = attention_scores + attention_mask

        # Normalize the attention scores to probabilities.
        # 使用 softmax 函数将注意力值标准化成概率值
        attention_probs = nn.Softmax(dim=-1)(attention_scores)
        # This is actually dropping out entire tokens to attend to, which might
        # seem a bit unusual, but is taken from the original Transformer paper.
        # Fixme
        attention_probs = self.attn_dropout(attention_probs)
        # context_layer = softmax(Q * K^T) * V, 尺寸为[B, N, S, H/N](32, 8, 128, 768/8)
        context_layer = torch.matmul(attention_probs, value_layer)
        # 调整维度， 尺寸为[B, S, N, H/N](32, 128, 8, 768/8)
        context_layer = context_layer.permute(0, 2, 1, 3).contiguous()
        # 调整维度，多头合并，尺寸为[B, S, H](32, 128, 768)
        new_context_layer_shape = context_layer.size()[
            :-2] + (self.all_head_size,)
        context_layer = context_layer.view(*new_context_layer_shape)
        hidden_states = self.dense(context_layer)
        hidden_states = self.out_dropout(hidden_states)
        hidden_states = self.LayerNorm(hidden_states + input_tensor)

        return hidden_states

    def forward_with_mask(self, input_tensor, attention_mask):
        # batch*1*1*seqlen 增加维度
        attention_mask = attention_mask.unsqueeze(1).unsqueeze(2)
        # padding 的 token置为负无穷
        attention_mask = (1.0 - attention_mask) * (-np.Inf)
        # Q K V 矩阵 尺寸为[B, S, H](32, 128, 768)
        mixed_query_layer = self.query(input_tensor)
        mixed_key_layer = self.key(input_tensor)
        mixed_value_layer = self.value(input_tensor)

        # 转置后Q K V 矩阵尺寸为[B, N, S, H/N](32, 8, 128, 768/8)
        query_layer = self.transpose_for_scores(mixed_query_layer)
        key_layer = self.transpose_for_scores(mixed_key_layer)
        value_layer = self.transpose_for_scores(mixed_value_layer)

        # 将"query"和"key"点乘，得到未经处理注意力值
        # attention_scores 尺寸为[B, N, S, S](32, 8, 128, 128)
        # Take the dot product between "query" and "key" to get the raw attention scores.
        attention_scores = torch.matmul(
            query_layer, key_layer.transpose(-1, -2))

        # 标准化，避免内积过大 1/sqrt(d_k)
        attention_scores = attention_scores / \
            math.sqrt(self.attention_head_size)

        # Apply the attention mask is (precomputed for all layers in BertModel forward() function)
        # [batch_size heads seq_len seq_len] scores
        # [batch_size 1 1 seq_len]
        attention_scores = attention_scores + attention_mask

        # Normalize the attention scores to probabilities.
        # 使用 softmax 函数将注意力值标准化成概率值
        attention_probs = nn.Softmax(dim=-1)(attention_scores)
        # This is actually dropping out entire tokens to attend to, which might
        # seem a bit unusual, but is taken from the original Transformer paper.
        # Fixme
        attention_probs = self.attn_dropout(attention_probs)
        # context_layer = softmax(Q * K^T) * V, 尺寸为[B, N, S, H/N](32, 8, 128, 768/8)
        context_layer = torch.matmul(attention_probs, value_layer)
        # 调整维度， 尺寸为[B, S, N, H/N](32, 128, 8, 768/8)
        context_layer = context_layer.permute(0, 2, 1, 3).contiguous()
        # 调整维度，多头合并，尺寸为[B, S, H](32, 128, 768)
        new_context_layer_shape = context_layer.size()[
            :-2] + (self.all_head_size,)
        context_layer = context_layer.view(*new_context_layer_shape)
        hidden_states = self.dense(context_layer)
        hidden_states = self.out_dropout(hidden_states)
        hidden_states = self.LayerNorm(hidden_states + input_tensor)

        return hidden_states
