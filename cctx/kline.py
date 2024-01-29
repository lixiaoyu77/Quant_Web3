import ccxt
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('expand_frame_repr', False)

okex = ccxt.okex({
    'timeout': 1000,
    'enableRateLimit': True,
    'apiKey': '-',
    'secret': '-',
})
okex.proxies = {
    'http': 'http://127.0.0.1:1087',
    'https': 'http://127.0.0.1:1087',
}

okex_markets = okex.load_markets()
# 打印okex交易所支持的Token
# print(okex_markets.keys())


btc_symbol = 'BTC/USDT'
eth_symbol = 'ETH/USDT'
bnb_symbol = 'BNB/USDT'
cfx_symbol = 'CFX/USDT'

if okex.has['fetchOHLCV']:
    kline_data = pd.DataFrame(okex.fetch_ohlcv(cfx_symbol, timeframe='1m', limit=300))
    kline_data.columns = ['Datetime', 'Open', 'High', 'Low', 'Close', 'Vol']
    kline_data['Datetime'] = kline_data['Datetime'].apply(okex.iso8601)
    print(kline_data.tail())
    # print(kline_data.shape)
    kline_data['Datetime'] = pd.to_datetime(kline_data['Datetime'])
    kline_data.set_index('Datetime', inplace=True)
    kline_data['Vol'].plot(figsize=(15, 8))

# 交易所最多获取300个数据，这个可以多获取
# if okex.has['fetchOHLCV']:
#     since = okex.parse8601('2023-05-17T07:00:00.000Z')
#     end = okex.milliseconds() - 60 * 1000
#     all_kline_data = []
#     while since < end:
#         symbol = 'CFX/USDT'
#         kline_data = okex.fetch_ohlcv(symbol, since=since, timeframe='1h', limit=300)
#         if len(kline_data):
#             # 更新获取时间
#             since = kline_data[len(kline_data)-1][0]
#             all_kline_data += kline_data
#         else:
#             break
#     all_kline_data_df = pd.DataFrame(all_kline_data)
#     all_kline_data_df.columns = ['Datetime', 'Open', 'High', 'Low', 'Close', 'Vol']
#     all_kline_data_df['Datetime'] = all_kline_data_df['Datetime'].apply(okex.iso8601)
    # print(all_kline_data_df)
    # print(all_kline_data_df.tail())
    # print(all_kline_data_df.shape)
    # 检查是否有重复数据
    # print(all_kline_data_df[all_kline_data_df['Datetime'].duplicated()])
    # 去除重复
    # all_kline_data_df.drop_duplicates(subset=['Datetime'], inplace=True)
    #
    # all_kline_data_df['Datetime'] = pd.to_datetime(all_kline_data_df['Datetime'])
    # all_kline_data_df.set_index('Datetime', inplace=True)
    # all_kline_data_df['Open'].plot(figsize=(15, 8))
    plt.title('CFX Open Price')
    plt.show()

