import torch
import torch.nn as nn


class SelfAttention(nn.Module):
    def __init__(self) -> None:
        super(SelfAttention, self).__init__()
