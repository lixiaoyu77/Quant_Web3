import pandas as pd
import crypto_data_utils as cdu

# 将中间省略号弄去
pd.set_option('expand_frame_repr', False)


def main():
    # 1.获取单个交易对的k想数据及处理
    symbol = 'BTC-USDT'
    # [1m/3m/5m/15m/30m/1H/2H/4H]
    bar = '1D'
    limit = 300
    kline_df = cdu.get_signal_kline_data(symbol, bar, limit)
    # print(ticker_df)
    print('获取单个交易对' + symbol + '的k线数据：')
    print(kline_df)
    kline_df.to_csv('CSV/BTC-USDT.csv', index=False)

    # 2.获取多个交易对的k想数据及处理
    # symbols = ['BTC-USDT', 'ETH-USDT', 'LINK-USDT']
    # # [1m/3m/5m/15m/30m/1H/2H/4H]
    # bar = '1H'
    # limit = 19
    # klines_df = cdu.get_lines_data(symbols, bar, limit)
    # # print(ticker_df)
    # print('获取多个交易对的k线数据：')
    # print(klines_df)


if __name__ == '__main__':
    main()
