from mydataloader import stock_price_by_minute_dataset
from torch.utils.data import DataLoader

model = stock_price_by_minute_dataset(dataloc='../../../data/000016_6_8_m1.csv')
model2 = DataLoader(dataset=model, batch_size=4, shuffle=True)
