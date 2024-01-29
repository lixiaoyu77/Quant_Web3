import requests
import pandas as pd
from datetime import datetime
import pytz

# 将中间省略号弄去
pd.set_option('expand_frame_repr', False)


# 1.获取单个交易对ticker的数据及处理
def get_signal_ticker_data(symbol):
    ticker_url = 'https://aws.okx.com/api/v5/market/ticker?instId={}'.format(symbol)
    try:
        res_obj = requests.get(ticker_url, timeout=15)
    except Exception as e:
        print('错误！', e)
        return None

    raw_df = None

    if res_obj.status_code == 200:
        json_obj = res_obj.json()
        if json_obj['code'] != '0':
            print('错误码：{}'.format(json_obj['code']))
        else:
            raw_df = pd.DataFrame(json_obj['data'])
            raw_df['ts'] = pd.to_datetime(datetime.now())
            raw_df['instId'] = symbol.replace('-', '/')
    else:
        print('状态码：{}'.format(res_obj.status_code))

    return raw_df


# 2.多个交易对ticker的数据及处理


def get_tickers_data(symbols):
    tickers_df = pd.DataFrame()
    for i, symbol in enumerate(symbols):
        ticker_df = get_signal_ticker_data(symbol)
        if ticker_df is not None:
            tickers_df = pd.concat([tickers_df, ticker_df], ignore_index=True)
        else:
            print(f"第{i + 1}个交易对 ({symbol}) 出错，请检查交易对是否正确")
    return tickers_df

# 1.获取单个交易对的k想数据及处理


def get_signal_kline_data(symbol, bar='1m', limit=20):
    kline_url = 'https://aws.okx.com/api/v5/market/candles?instId={}&bar={}&limit={}' \
        .format(symbol, bar, limit, )
    try:
        res_obj = requests.get(kline_url, timeout=15)
    except Exception as e:
        print('错误！', e)
        return None

    kline_df = None

    if res_obj.status_code == 200:
        json_obj = res_obj.json()
        if json_obj['code'] != '0':
            print('错误码：{}'.format(json_obj['code']))
        else:
            raw_df = pd.DataFrame(json_obj['data'])
            kline_df = raw_df.copy()
            kline_df.columns = ['datetime', 'open', 'high', 'low', 'close', 'vol', 'volCcy', 'volCcyQuote', 'confirm']
            kline_df['datetime'] = kline_df['datetime'].astype(int)

            # 默认为UTF+0时间
            kline_df['datetime'] = pd.to_datetime(kline_df['datetime'], unit='ms')

            # 将 UTC 时间转换为本地时间（UTC+8）
            # utc_time = pd.to_datetime(kline_df['datetime'], unit='ms', utc=True)
            # local_time = utc_time.dt.tz_convert(pytz.timezone('Asia/Shanghai'))
            # kline_df['datetime'] = local_time

    else:
        print('状态码：{}'.format(res_obj.status_code))

    return kline_df


# 1.获取多个交易对的k想数据及处理


def get_lines_data(symbols, bar='1m', limit=20):
    klines_df = pd.DataFrame()
    for i, symbol in enumerate(symbols):
        kline_df = get_signal_kline_data(symbol, bar, limit)
        if kline_df is not None:
            klines_df = pd.concat([klines_df, kline_df], ignore_index=True)
        else:
            print(f"第{i + 1}个交易对 ({symbol}) 出错，请检查交易对是否正确")
    return klines_df
