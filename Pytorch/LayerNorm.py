import torch
import torch.nn as nn


class LayerNorm(nn.Module):
    "Construct a layernorm module (See citation for details)."
    # hidden_size

    def __init__(self, features, eps=1e-6):
        super(LayerNorm, self).__init__()
        self.a_2 = nn.Parameter(torch.ones(features))
        self.b_2 = nn.Parameter(torch.zeros(features))
        self.eps = eps

    def forward(self, x):
        # [B,S,H] → [B,S,1]
        mean = x.mean(-1, keepdim=True)
        # [B,S,H] → [B,S,1]
        std = x.std(-1, keepdim=True)
        # 等价于(x-mean) / std 不同的是保留那些东西了。
        return self.a_2 * (x - mean) / (std + self.eps) + self.b_2
