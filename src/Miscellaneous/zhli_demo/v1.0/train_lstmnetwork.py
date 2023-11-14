import mydataloader
import lstmnetwork
from torch.utils.data import DataLoader
import torch.nn as nn
from torch import optim

inputdim = 25

batch_s = 20
stockdataset = mydataloader.stock_price_by_minute_dataset(dataloc='../../data/000016_6_8_m1.csv')
stockdataloader = DataLoader(dataset=stockdataset, batch_size=batch_s, shuffle=True)
# 定义loss
criterion = nn.MSELoss()
# 定义优化器
Learning_rate = 0.001
train_model = lstmnetwork.LSTM(input_dim=inputdim)
optimizer = optim.Adam(train_model.parameters(), lr=Learning_rate)  # 使用 Adam 优化器 比课上使用的 SGD 优化器更加稳定
lstm_losses = []
n_epochs = 50
# 开始训练
for epoch in range(n_epochs):
    for iter_, (x, label) in enumerate(stockdataloader):
        if (x.shape[0] != batch_s):
            continue

        pred, (h1, c1) = train_model(x)

        # 梯度复位
        optimizer.zero_grad()

        # 定义损失函数
        loss = criterion(pred, label)

        # 反向求导
        loss.backward(retain_graph=True)

        # 梯度迭代
        optimizer.step()

        # 记录loss
        lstm_losses.append(loss.item())
print(lstm_losses)
