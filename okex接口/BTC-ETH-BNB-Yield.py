import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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


BTC_df['profit'] = BTC_df['close'].pct_change(1)
ETH_df['profit'] = ETH_df['close'].pct_change(1)
BNB_df['profit'] = BNB_df['close'].pct_change(1)
# print(ETH_df['profit'])

# 使用直方图查看BTC收益率的稳定性
# BTC_df['profit'].hist(bins=100, label='BTC/USDT', figsize=(10, 8), alpha=0.5)
# ETH_df['profit'].hist(bins=100, label='ETH/USDT', alpha=0.5)
# BNB_df['profit'].hist(bins=100, label='BNB/USDT', alpha=0.5)

# 使用盒子图比较不同加密货币的日收益率
Yield_df = pd.concat([BTC_df['profit'], ETH_df['profit'], BNB_df['profit']], axis=1)
Yield_df.columns = ['BTC Yield', 'ETH Yield', 'BNB Yield']
# print(Yield_df.head())

plt.figure(figsize=(10, 8))
sns.boxplot(data=Yield_df)
plt.title('BTC-ETH-BNB Daily Profit')
# plt.legend()
plt.show()
