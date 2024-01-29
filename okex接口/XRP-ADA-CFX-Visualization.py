import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('expand_frame_repr', False)

XRP_df = pd.read_csv('CSV/XRP-USDT-DATA.csv', index_col='datetime', parse_dates=True)
ADA_df = pd.read_csv('CSV/ADA-USDT-DATA.csv', index_col='datetime', parse_dates=True)
CFX_df = pd.read_csv('CSV/CFX-USDT-DATA.csv', index_col='datetime', parse_dates=True)


if XRP_df.index.duplicated().any():
    print('XRP索引去重')
    XRP_df = XRP_df[~XRP_df.index.duplicated()]
if ADA_df.index.duplicated().any():
    print('ETH索引去重')
    ADA_df = ADA_df[~ADA_df.index.duplicated()]
if CFX_df.index.duplicated().any():
    print('CFX索引去重')
    CFX_df = CFX_df[~CFX_df.index.duplicated()]
# 收盘价格
XRP_df['close'].plot(label='XRP/USDT', figsize=(16, 8), title='Price')
ADA_df['close'].plot(label='ADA/USDT')
CFX_df['close'].plot(label='CFX/USDT')
# 交易量
# XRP_df['vol'].plot(label='XRP/USDT', figsize=(16, 8), title='Volume Traded')
# ADA_df['vol'].plot(label='ADA/USDT')
# CFX_df['vol'].plot(label='CFX/USDT')

plt.legend()  # 显示该 label 的内容
plt.show()
