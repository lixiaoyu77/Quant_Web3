import pandas as pd
import matplotlib.pyplot as plt
pd.set_option('expand_frame_repr', False)

# 重采样
df = pd.read_csv('CSV/ETH-USDT.csv')

# 必须这样才可以重采样
df['datetime'] = pd.to_datetime((df['datetime']))
df.set_index('datetime', inplace=True)

# 一步就可以重采样
df2 = pd.read_csv('CSV/BTC-USDT.csv', index_col='datetime', parse_dates=True)
# print(df.head())
# print(df.info())

# print(df.resample(rule='A').mean())
# print(df.resample(rule='Q').mean())


# plt.figure(figsize=(8, 5))
# 画线
# df['close'].resample('W').mean().plot(kind='line')

# 均线平移
# df['close'].plot()
# df['close'].rolling(window=5).mean().plot(figsize=(16, 6))
# df['close'].rolling(window=7).mean().plot(figsize=(16, 6))
# df['close'].rolling(window=30).mean().plot(figsize=(16, 6))

df['close_MA5'] = df['close'].rolling(window=5).mean()
df['close_MA7'] = df['close'].rolling(window=7).mean()
df['close_MA30'] = df['close'].rolling(window=30).mean()
df[['close','close_MA5','close_MA7','close_MA30']].plot(figsize=(16, 6))

plt.title('ETH Close Moving Average')
plt.show()