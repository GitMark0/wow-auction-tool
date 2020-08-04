from model import NN
import torch
import numpy as np
import pandas as pd
from data_preparation import encode


def predict(X):
    nn = NN([6, 8, 4, 1])
    nn.load_state_dict(torch.load('model_state/state'))
    nn.eval()
    result = nn.forward(X)
    return result.detach().numpy()


if __name__ == '__main__':

    print('quantity, price, dow, month')
    vals = input().split()
    val_dict = {'quantity': [float(vals[0])], 'price': [float(vals[1])], 'dow': [int(vals[2])], 'month': [int(vals[3])]}

    # Normalize quantity, magic numbers. Log price.
    vals_df = pd.DataFrame(val_dict)
    vals_df['quantity'] = (vals_df['quantity'] - 670) / (65535 - 670)
    vals_df['price'] = np.log(vals_df['price'])
    vals_df = encode(vals_df, 'month', 12)
    vals_df = encode(vals_df, 'dow', 6)
    vals_df = vals_df.drop('month', axis=1)
    vals_df = vals_df.drop('dow', axis=1)
    X = vals_df.values
    X = torch.from_numpy(X).float()
    val = predict(X)
    print(val)
