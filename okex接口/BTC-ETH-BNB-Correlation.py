import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
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

coins_index = BNB_df.index
coins_df = pd.DataFrame(columns=['BTC/USDT', 'ETH/USDT', 'BNB/USDT'], index=BNB_df.index)

coins_df['BTC/USDT'] = BTC_df['close']
coins_df['ETH/USDT'] = ETH_df['close']
coins_df['BNB/USDT'] = BNB_df['close']

# 可视化相关性
# scatter_matrix(coins_df, figsize=(10, 10), hist_kwds={'bins': 100})
# pairplot可视化相关性
# sns.pairplot(coins_df)
# 使用corr()量化相关性
print(coins_df.corr())

# plt.legend()
# plt.show()
