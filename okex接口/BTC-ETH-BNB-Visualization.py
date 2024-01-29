import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('expand_frame_repr', False)

BTC_df = pd.read_csv('CSV/BTC-USDT-DATA.csv', index_col='datetime', parse_dates=True)
ETH_df = pd.read_csv('CSV/ETH-USDT-DATA.csv', index_col='datetime', parse_dates=True)
BNB_df = pd.read_csv('CSV/BNB-USDT-DATA.csv', index_col='datetime', parse_dates=True)

# 检查是否有重复的index
# print(BTC_df[BTC_df.index.duplicated()])
# print(ETH_df[ETH_df.index.duplicated()])
# print(BNB_df[BNB_df.index.duplicated()])
if BTC_df.index.duplicated().any():
    print('BTC索引去重')
    BTC_df = BTC_df[~BTC_df.index.duplicated()]
if ETH_df.index.duplicated().any():
    print('ETH索引去重')
    ETH_df = ETH_df[~ETH_df.index.duplicated()]
if BNB_df.index.duplicated().any():
    print('BNB索引去重')
    BNB_df = BNB_df[~BNB_df.index.duplicated()]

# BTC_df['close'].plot(label='BTC/USDT', figsize=(16, 8), title='Volume Traded')
# ETH_df['close'].plot(label='ETH/USDT')
# BNB_df['close'].plot(label='BNB/USDT')

BTC_df['vol'].plot(label='BTC/USDT', figsize=(16, 8), title='Volume Traded')
ETH_df['vol'].plot(label='ETH/USDT')
BNB_df['vol'].plot(label='BNB/USDT')
plt.legend()
plt.show()