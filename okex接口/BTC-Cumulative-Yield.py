import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('expand_frame_repr', False)

BTC_df = pd.read_csv('CSV/BTC-USDT-DATA.csv', index_col='datetime', parse_dates=True)


if BTC_df.index.duplicated().any():
    print('BTC索引去重')
    BTC_df = BTC_df[~BTC_df.index.duplicated()]

# 累计收益率计算 从第一天开始 Pt/P1
BTC_df['cumulative profit'] = BTC_df['close']/BTC_df.iloc[0]['close'] - 1
# print(BTC_df.head())

# 使用直方图查看BTC收益率的稳定性
# BTC_df['cumulative profit'].hist(bins=100)
BTC_df['cumulative profit'].plot(label='BTC/USDT', figsize=(16, 8))

plt.title('BTC Cumulative Profit')
# plt.legend()
plt.show()