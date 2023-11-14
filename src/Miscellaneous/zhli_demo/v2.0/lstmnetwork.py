import torch.nn as nn
import torch


# input_dim = 4      # 数据的特征数
# hidden_dim = 32    # 隐藏层的神经元个数
# num_layers = 2     # LSTM的层数
# output_dim = 1     # 预测值的特征数
class LSTM(nn.Module):
    def __init__(self, input_dim, output_dim=1, hidden_dim=16):
        super(LSTM, self).__init__()
        # Hidden dimensions
        self.mlpoutsize = 8
        self.mlphidsize = 64
        # Number of hidden layers
        # Building your LSTM
        # batch_first=True causes input/output tensors to be of shape (batch_dim, seq_dim, feature_dim)
        self.lin1 = nn.Linear(input_dim, self.mlphidsize)
        self.acti1 = nn.ReLU()
        self.lin2 = nn.Linear(self.mlphidsize, self.mlpoutsize)
        self.acti2 = nn.ReLU()
        # self.lin3 = nn.Linear(self.mlpoutsize,self.mlpoutsize)
        # self.acti3 = nn.ReLU()
        self.lstm = nn.LSTM(self.mlpoutsize, hidden_dim, num_layers=2, batch_first=True)
        # Readout layer 在LSTM后再加一个全连接层，因为是回归问题，所以不能在线性层后加激活函数
        self.fc = nn.Linear(hidden_dim, output_dim)

    def forward(self, x):
        x = self.lin1(x)
        x = self.acti1(x)
        x = self.lin2(x)
        x = self.acti2(x)
        res, (hidden, cell) = self.lstm(x)
        out = self.fc(res)
        return out
