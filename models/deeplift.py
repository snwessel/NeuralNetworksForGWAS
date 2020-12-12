"""
An example model that has double the number of convolutional layers
that DeepSEA (Zhou & Troyanskaya, 2015) has. Otherwise, the architecture
is identical to DeepSEA.
When making a model architecture file of your own, please review this
file in its entirety. In addition to the model class, Selene expects
that `criterion` and `get_optimizer(lr)` are also specified in this file.
"""
import numpy as np
import torch
import torch.nn as nn


class DeepLIFT(nn.Module):
    """
    A DeepLIFT model architecture.
    Parameters
    ----------
    sequence_length : int
        The length of the sequences on which the model trains and and makes
        predictions.
    n_targets : int
        The number of targets (classes) to predict.
    Attributes
    ----------
    classifier : torch.nn.Sequential
        The linear classifier and sigmoid transformation components of the
        model.
    """

    def __init__(self, sequence_length, n_targets):
        super(DeepLIFT, self).__init__()
        hidden_size1 = 8000
        hidden_size2 = 1000

        # fully connected layer
        self.classifier = nn.Sequential(
            nn.Linear(4000, hidden_size1),
            nn.ReLU(inplace=True),
            nn.Linear(hidden_size1, hidden_size2),
            nn.ReLU(inplace=True),
            nn.BatchNorm1d(hidden_size2),
            nn.Linear(hidden_size2, n_targets),
            nn.Sigmoid())

    def forward(self, x):
        """
        Forward propagation of a batch.
        """
        #print(x.shape)
        reshape_x = x.reshape(x.size(0), 4000)
        out = self.classifier(reshape_x)
        return out

def criterion():
    """
    Specify the appropriate loss function (criterion) for this
    model.
    Returns
    -------
    torch.nn._Loss
    """
    return nn.MSELoss()

def get_optimizer(lr):
    """
    Specify an optimizer and its parameters.
    Returns
    -------
    tuple(torch.optim.Optimizer, dict)
        The optimizer class and the dictionary of kwargs that should
        be passed in to the optimizer constructor.
    """
    return (torch.optim.SGD,
            {"lr": lr, "weight_decay": 1e-6, "momentum": 0.9})
            