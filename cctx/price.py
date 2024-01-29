import ccxt

okex = ccxt.okex({
    'timeout': 1000,
    'enableRateLimit': True,
    'apiKey': 'ee98612e-1935-4df4-8a48-94b1a0731e60',
    'secret': 'BEE9431441052767ECFF54B8AF6E772A',
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

# 获取单个交易对
btc_usdt_market = okex_markets[btc_symbol]
# print(btc_usdt_market)

# 获取单个交易对实时数据
ticker_data = okex.fetch_ticker(cfx_symbol)
# print(ticker_data)
print(f'{cfx_symbol}的Ticker最新Price:', ticker_data['last'])

# 获取多个交易对实时数据
symbols = ['BTC/USDT', 'ETH/USDT']
tickers_data = okex.fetch_tickers(symbols)
# print(tickers_data)
# print(f'{symbols[1]}的Ticker最新Price:', tickers_data['ETH/USDT']['last'])

# 获取单个交易对交易委托账本信息
# bid 买价
# ask 卖出
# 价差 ask-bid 体现市场流动性
order_book = okex.fetch_order_book(btc_symbol)
# print(order_book)
# 获取最高买价和卖价
bid = order_book['bids'][0][0] if len(order_book['bids']) > 0 else None
ask = order_book['asks'][0][0] if len(order_book['asks']) > 0 else None
# 价差
spread = (ask-bid) if (bid and ask) else None
# print('买价：{:.2f}， 卖价：{:.2f}, 价差：{:.2f}'.format(bid, ask, spread))


