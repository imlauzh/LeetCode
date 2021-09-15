import torch
import torch.nn as nn


class LayerNorm(torch.nn.Module):
    # pylint: disable=line-too-long
    """
    An implementation of `Layer Normalization
    <https://www.semanticscholar.org/paper/Layer-Normalization-Ba-Kiros/97fb4e3d45bb098e27e0071448b6152217bd35a5>`_ .

    Layer Normalization stabilises the training of deep neural networks by
    normalising the outputs of neurons from a particular layer. It computes:

    output = (gamma * (tensor - mean) / (std + eps)) + beta

    Parameters
    ----------
    dimension : ``int``, required.
        The dimension of the layer output to normalize.
    eps : ``float``, optional, (default = 1e-6)
        An epsilon to prevent dividing by zero in the case
        the layer has zero variance.

    Returns
    -------
    The normalized layer output.
    """

    def __init__(self,
                 dimension: int,
                 eps: float = 1e-6) -> None:
        super().__init__()
        self.gamma = nn.Parameter(torch.ones(dimension))
        self.beta = nn.Parameter(torch.zeros(dimension))
        self.eps = eps

    def forward(self, tensor: torch.Tensor):  # pylint: disable=arguments-differ
        # 注意，是针对最后一个维度进行求解~
        mean = tensor.mean(-1, keepdim=True)
        std = tensor.std(-1, unbiased=False, keepdim=True)
        return self.gamma * (tensor - mean) / (std + self.eps) + self.beta


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