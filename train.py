import numpy as np
import pandas as pd
import torch
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from model import NN
import matplotlib.pyplot as plt

scaler = MinMaxScaler()


def plot_results(model, X, y):
    X, X_test, y, y_test = train_test_split(X, y, test_size=0.15, random_state=42)
    days_train = [i for i in range(X.shape[0])]
    days_test = [i for i in range(X_test.shape[0])]
    X = torch.from_numpy(X).float()
    X_test = torch.from_numpy(X_test).float()
    y_train_ = model.forward(X).detach().numpy()
    y_test_ = model.forward(X_test).detach().numpy()
    plt.figure(figsize=(10, 10))
    plt.subplot(211)
    plt.title('train_set')
    plt.plot(days_train, y_train_, label='predicted')
    plt.plot(days_train, y, label='truth')
    plt.legend()
    plt.subplot(212)
    plt.title('test_set')
    plt.plot(days_test, y_test_, label='predicted')
    plt.plot(days_test, y_test, label='truth')
    plt.legend()
    plt.show()


def train(model, X, y, param_niter, param_delta):
    """Arguments:
       - X: model inputs [NxD], type: torch.Tensor
       - Yoh_: ground truth [NxC], type: torch.Tensor
       - param_niter: number of training iterations
       - param_delta: learning rate
    """
    # Nasumično uzimanje 15% podataka za validaciju
    X, X_test, y, y_test = train_test_split(X, y, test_size=0.15, random_state=42)
    X = torch.from_numpy(X).float()
    y = torch.from_numpy(y).float()
    X_test = torch.from_numpy(X_test).float()
    y_test = torch.from_numpy(y_test).float()
    criterion = torch.nn.MSELoss()
    last_loss_test = 999
    stop_count = 0
    # inicijalizacija optimizatora
    # ...
    optimizer = torch.optim.SGD(model.parameters(), lr=param_delta, weight_decay=0.3)
    for epoch in range(param_niter):
        y_pred = model.forward(X)
        loss = criterion(y, y_pred)
        y_pred_test = model.forward(X_test)
        loss_test = criterion(y_test, y_pred_test)
        if loss_test >= last_loss_test:
            stop_count += 1
        if stop_count > 0 and loss_test < last_loss_test:
            stop_count -= 1
        if stop_count >= 5:
            print('Early stopping')
            break
        last_loss_test = loss_test
        print('epoch {}, loss - {}'.format(epoch, loss))
        print('test loss - {}'.format(loss_test))
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()


if __name__ == '__main__':
    data = pd.read_csv('datasets/anchor-weed.csv')
    scaler.fit_transform(data[['price']])

    np.random.seed(100)
    nr_classes = 6
    hidden_size = 12
    data = pd.read_csv('datasets/anchor-weed-prepared.csv')
    data = data.drop('Unnamed: 0', axis=1)
    y = data['price+1'].values
    X = data.drop('price+1', axis=1).values
    model = NN([nr_classes, 8, 4, 1])
    train(model, X, y, 30000, 0.01)
    torch.save(model.state_dict(), 'model_state/state')

    y_pred = model.forward(torch.from_numpy(X[275, :]).float())
    y_pred = np.exp(y_pred.detach().numpy().reshape(-1, 1))
    y_ = np.exp(y[275])

    plot_results(model, X, y)
