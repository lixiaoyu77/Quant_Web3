import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('expand_frame_repr', False)

BTC_df = pd.read_csv('CSV/BTC-USDT-DATA.csv', index_col='datetime', parse_dates=True)
ETH_df = pd.read_csv('CSV/ETH-USDT-DATA.csv', index_col='datetime', parse_dates=True)
BNB_df = pd.read_csv('CSV/BNB-USDT-DATA.csv', index_col='datetime', parse_dates=True)

if BTC_df.index.duplicated().any():
    print('BTC索引去重')
    BTC_df = BTC_df[~BTC_df.index.duplicated()]
if ETH_df.index.duplicated().any():
    print('ETH索引去重')
    ETH_df = ETH_df[~ETH_df.index.duplicated()]
if BNB_df.index.duplicated().any():
    print('BNB索引去重')
    BNB_df = BNB_df[~BNB_df.index.duplicated()]


# 累计收益率计算 从第一天开始 Pt/P1
BTC_df['cumulative profit'] = BTC_df['close']/BTC_df.iloc[0]['close'] - 1
ETH_df['cumulative profit'] = ETH_df['close']/ETH_df.iloc[0]['close'] - 1
BNB_df['cumulative profit'] = BNB_df['close']/BNB_df.iloc[0]['close'] - 1

# print(BTC_df.head())

# 使用折线图查看BTC总收益率
BTC_df['cumulative profit'].plot(label='BTC/USDT', figsize=(16, 8))
ETH_df['cumulative profit'].plot(label='ETH/USDT')
BNB_df['cumulative profit'].plot(label='BNB/USDT')

plt.title('BTC-ETH-BNB Cumulative Profit')
plt.legend()
plt.show()