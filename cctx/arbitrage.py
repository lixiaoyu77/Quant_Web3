import ccxt
import pandas as pd
import time

pd.set_option('expand_frame_repr', False)


def main():
    # 初始化交易所
    okex = ccxt.okex({
        'timeout': 1000,
        'enableRateLimit': True,
        'apiKey': 'ee98612e-1935-4df4-8a48-94b1a0731e60',
        'secret': 'BEE9431441052767ECFF54B8AF6E772A',
        'password': '@Qq18779928336'
    })
    okex.proxies = {
        'http': 'http://127.0.0.1:1087',
        'https': 'http://127.0.0.1:1087',
    }
    # 加载行情
    markets = okex.load_markets()
    # print(markets.keys())

    # 选择两个交易市场 A B
    market_a = 'BTC'
    market_b = 'ETH'

    symbols = list(markets.keys())

    symbols_df = pd.DataFrame(data=symbols, columns=['symbol'])
    # 分割字符串，得到基础货币/计价货币
    base_quote_df = symbols_df['symbol'].str.split(pat='/', expand=True)
    base_quote_df.columns = ['base', 'quote']

    # 过滤得到以A,B 计价的计价货币
    base_a_list = base_quote_df[base_quote_df['quote'] == market_a]['base'].values.tolist()
    base_b_list = base_quote_df[base_quote_df['quote'] == market_b]['base'].values.tolist()

    # 获取相同的基础货币列表
    common_base_list = list(set(base_a_list).intersection(set(base_b_list)))
    print('{}和{}有{}个相同的计价货币'.format(market_a, market_b, len(common_base_list)))

    # 执行套利步骤
    columns = ['Market A', 'Market B', 'Market C', 'P1', 'P2', 'P3', 'Profit(%)']

    results_df = pd.DataFrame(columns=columns)

    # 获取前一分钟的close的价格
    last_min = okex.milliseconds() - 60 * 1000
    for base_coin in common_base_list:
        market_c = base_coin
        market_a2b_symbol = '{}/{}'.format(market_b,market_a)
        market_b2c_symbol = '{}/{}'.format(market_c,market_b)
        market_a2c_symbol = '{}/{}'.format(market_c,market_a)
        # 获取前一分钟的kline
        market_a2b_kline = okex.fetch_ohlcv(market_a2b_symbol, since=last_min, limit=1, timeframe='1m')
        market_b2c_kline = okex.fetch_ohlcv(market_b2c_symbol, since=last_min, limit=1, timeframe='1m')
        market_a2c_kline = okex.fetch_ohlcv(market_a2c_symbol, since=last_min, limit=1, timeframe='1m')
        if len(market_a2b_kline) == 0 or len(market_b2c_kline) == 0 or len(market_a2c_kline) == 0:
            continue
        # 获取前一分钟的kline的价格
        p1 = market_a2b_kline[0][4]
        p2 = market_b2c_kline[0][4]
        p3 = market_a2c_kline[0][4]
        # 价差
        profit = (p3 / (p1 * p2) - 1) * 1000

        results_df = results_df._append({
            'Market A': market_a,
            'Market B': market_b,
            'Market C': market_c,
            'P1': p1,
            'P2': p2,
            'P3': p3,
            'Profit(%)': profit
        }, ignore_index=True)

        print(results_df.tail(1))

        time.sleep(okex.rateLimit / 1000)

    results_df.to_csv('./tri_arbitrage.csv', index=None)

if __name__ == '__main__':
    main()