import torch


class NN(torch.nn.Module):
    def __init__(self, layers):
        super(NN, self).__init__()
        self.hidden = torch.nn.ModuleList()
        for i in range(len(layers) - 1):
            self.hidden.append(torch.nn.Linear(layers[i], layers[i + 1]))
        self.relu = torch.nn.ReLU()

    def forward(self, x):
        for i in range(len(self.hidden)):
            x = self.hidden[i](x)
            if i != len(self.hidden)-1:
                x = self.relu(x)
        return x
