import torch


def predict(data):
    # simple mock — later load real model
    return torch.tensor(sum(data.values())).item()
