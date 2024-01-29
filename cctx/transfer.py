import ccxt

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

print('总共的BTC', okex.fetch_balance()['total']['USDT'])
print('可用的BTC', okex.fetch_balance()['free']['USDT'])
print('冻结的BTC', okex.fetch_balance()['used']['USDT'])

# 下单
# limit/market 市价和限价
# if okex.has['createLimitOrder']:
# okex.create_order(symbol='CFX/USDT', side='buy', amount=1, price=0.1, type='limit')
# okex.create_order(symbol='BTC/USDT', side='sell', amount=0.1, price=60000, type='limit')

# 查询订单
open_orders = okex.fetch_open_orders('CFX/USDT')
# print(open_order)

# 取消订单
# if okex.has['cancelOrder']:
#     for order in open_orders:
#         order_id = order['info']['orderId']
#         okex.cancel_order(order_id, 'CFX/USDT')

# 查询以前的订单
if okex.has['fetchClosedOrders']:
    closed_orders = okex.fetch_closed_orders('CFX/USDT')
    for close_order in closed_orders:
        print(close_order)
