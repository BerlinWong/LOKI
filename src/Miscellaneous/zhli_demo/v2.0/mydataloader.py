from torch.utils.data import Dataset
from torch.utils.data import DataLoader
import pandas as pd
import torch


class stock_price_by_minute_dataset(Dataset):
    # 设置全局参数
    def __init__(self, input_tdim=5, input_wint_dim=10, dataloc='../../../data/000016_6_8_m1.csv'):
        self.input_tdim = input_tdim
        self.input_wint_dim = input_wint_dim
        self._data = pd.read_csv(dataloc)['close']
        self.data = self._data.values.reshape((-1, 240))

    def __getitem__(self, item):
        day_msg = item // (240 - self.input_tdim)
        tim_msg = item % (240 - self.input_tdim)
        input_prices = self.data[day_msg:day_msg + self.input_wint_dim, tim_msg:tim_msg + self.input_tdim]
        input_prices = input_prices.reshape(-1)
        input_prices_tensor = torch.from_numpy(input_prices).float()
        label = self.data[day_msg + self.input_wint_dim - 1, tim_msg + self.input_tdim] - \
                self.data[day_msg + self.input_wint_dim - 1, tim_msg + self.input_tdim - 1]
        return input_prices_tensor, label

    # 列表有多长
    def __len__(self):
        return (self.data.shape[0] - self.input_wint_dim + 1) * (self.data.shape[1] - self.input_tdim)
