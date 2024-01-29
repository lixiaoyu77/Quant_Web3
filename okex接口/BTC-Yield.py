import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('expand_frame_repr', False)

BTC_df = pd.read_csv('CSV/BTC-USDT-DATA.csv', index_col='datetime', parse_dates=True)


if BTC_df.index.duplicated().any():
    print('BTC索引去重')
    BTC_df = BTC_df[~BTC_df.index.duplicated()]

# 日收益率计算 Rt = (Pt/Pt-1) - 1
# 方法一 使用shift计算
# BTC_df['profit'] = (BTC_df['close']/BTC_df['close'].shift(1))-1
# 方法二 使用pct_change
BTC_df['profit'] = BTC_df['close'].pct_change(1)
# print(BTC_df.head())

# 使用直方图查看BTC收益率的稳定性
# BTC_df['profit'].hist(bins=100)
# plt.title('BTC Daily Profit')
# plt.legend()
plt.show()
