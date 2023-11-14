from torch.utils.data import Dataset
from torch.utils.data import DataLoader
import pandas as pd
import torch


class stock_price_by_minute_dataset(Dataset):
    # 设置全局参数
    def __init__(self, dataloc='../../data/000016_6_8_m1.csv'):
        self.input_tdim = 5
        self.data = pd.read_csv(dataloc)

    def __getitem__(self, item):
        input_prices = self.data.iloc[item:item + self.input_tdim, -5:].values
        input_prices = input_prices.reshape(-1)
        input_prices_tensor = torch.from_numpy(input_prices).float()
        label = self.data.iloc[item + self.input_tdim + 1, -5] - self.data.iloc[item + self.input_tdim, -5]
        return input_prices_tensor, label

    # 列表有多长
    def __len__(self):
        return self.data.shape[0] - self.input_tdim
