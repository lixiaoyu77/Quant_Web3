import requests
import pandas as pd
from datetime import datetime
import crypto_data_utils as cdu

# 将中间省略号弄去
pd.set_option('expand_frame_repr', False)

def main():
    # 交易所API初体验
    # 1.获取单个交易对ticker的数据及处理
    symbol = 'BTC-USDT'
    ticker_df = cdu.get_signal_ticker_data(symbol)
    # print(ticker_df)
    print('获取单个交易对数据：')
    print(ticker_df[['ts', 'instId', 'last', 'askPx', 'askSz', 'bidPx', 'bidSz', ]])

    # 2.多个交易对ticker的数据及处理
    symbols = ['BTC-USDT', 'ETH-USDT', 'CFX-USDT']
    tickers_df = cdu.get_tickers_data(symbols)
    # print(tickers_df)
    print('获取多个交易对数据：')
    print(tickers_df[['ts', 'instId', 'last', 'askPx', 'askSz', 'bidPx', 'bidSz', ]])


if __name__ == '__main__':
    main()
