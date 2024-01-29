from datetime import datetime
import pandas as pd
import crypto_data_utils as cdu


def main():
    # 1.获取单个交易对的k想数据及处理
    # [1m/3m/5m/15m/30m/1H/2H/4H]
    # 香港时间开盘价k线：[6H / 12H / 1D / 1W / 1M]
    # UTC时间开盘价k线：[6Hutc / 12Hutc / 1Dutc / 1Wutc / 1Mutc]
    BTC_df = cdu.get_signal_kline_data(symbol='BTC-USDT', bar='1D', limit=100)
    ETH_df = cdu.get_signal_kline_data(symbol='ETH-USDT', bar='1D', limit=100)
    BNB_df = cdu.get_signal_kline_data(symbol='BNB-USDT', bar='1D', limit=100)

    # 在数据里面加一个symbol
    BTC_df['symbol'] = 'BTC/USDT'
    ETH_df['symbol'] = 'ETH/USDT'
    BNB_df['symbol'] = 'BNB/USDT'

    print(' BTC-USDT 的k线数据如下：')
    print(BTC_df)
    print(' ETH-USDT 的k线数据如下：')
    print(ETH_df)
    print(' BNB-USDT 的k线数据如下：')
    print(BNB_df)

    BTC_df.to_csv('CSV/BTC-USDT-DATA.csv', index=False)
    ETH_df.to_csv('CSV/ETH-USDT-DATA.csv', index=False)
    BNB_df.to_csv('CSV/BNB-USDT-DATA.csv', index=False)


if __name__ == '__main__':
    main()
