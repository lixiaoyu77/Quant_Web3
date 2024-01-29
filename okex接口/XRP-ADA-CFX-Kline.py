from datetime import datetime
import pandas as pd
import crypto_data_utils as cdu


def main():
    # 1.获取单个交易对的k想数据及处理
    # [1m/3m/5m/15m/30m/1H/2H/4H]
    # 香港时间开盘价k线：[6H / 12H / 1D / 1W / 1M]
    # UTC时间开盘价k线：[6Hutc / 12Hutc / 1Dutc / 1Wutc / 1Mutc]

    XRP_df = cdu.get_signal_kline_data(symbol='XRP-USDT', bar='1D', limit=300)
    ADA_df = cdu.get_signal_kline_data(symbol='ADA-USDT', bar='1D', limit=300)
    CFX_df = cdu.get_signal_kline_data(symbol='CFX-USDT', bar='1D', limit=300)
    print(' XRP-USDT 的k线数据如下：')
    print(XRP_df)
    print(' ADA-USDT 的k线数据如下：')
    print(ADA_df)
    print(' CFX-USDT 的k线数据如下：')
    print(CFX_df)

    XRP_df.to_csv('CSV/XRP-USDT-DATA.csv', index=False)
    ADA_df.to_csv('CSV/ADA-USDT-DATA.csv', index=False)
    CFX_df.to_csv('CSV/CFX-USDT-DATA.csv', index=False)


if __name__ == '__main__':
    main()
