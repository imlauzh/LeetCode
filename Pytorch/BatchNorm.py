import torch
import torch.nn as nn


def bn_from_scratch(inputs):
    """do batch normalization when train without scale and shift
    :param: [batch_size, channels, height, width]
    """
    # compute mean over channels
    mean = torch.mean(inputs, dim=(0, 2, 3))
    # reshape for broadcast
    mean = mean.view(1, inputs.size(1), 1, 1)
    # compute std using biased way, plus epsilon for stability
    std = torch.sqrt(torch.var(inputs, dim=(0, 2, 3), unbiased=False) + 1e-5)
    std = std.view(1, inputs.size(1), 1, 1)
    invstd = 1/std
    # Core steps, do scale and shift here if wanted
    test_outputs = (inputs-mean)*invstd
    return test_outputs
