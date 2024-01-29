import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('expand_frame_repr', False)

CFX_df = pd.read_csv('CSV/BTC-USDT-DATA.csv', index_col='datetime', parse_dates=True)


if CFX_df.index.duplicated().any():
    print('BTC索引去重')
    CFX_df = CFX_df[~CFX_df.index.duplicated()]

# 添加收益率列
CFX_df['profit'] = CFX_df['close'].pct_change(1)

# 假设每天定投1000美元
invest_amount = 100

# 计算成本基础
CFX_df['cost_basis'] = invest_amount / CFX_df['close']

# 计算持有数量
CFX_df['holdings'] = CFX_df['cost_basis'].cumsum()

# 计算当前市值
CFX_df['market_value'] = CFX_df['holdings'] * CFX_df['close']

# 计算总成本
total_cost = (CFX_df['cost_basis'] * invest_amount).sum()

# 计算当前总收益
current_total_profit = CFX_df['market_value'][-1] - total_cost

# 计算当前总收益率
current_total_return = current_total_profit / total_cost

print('每日定投BTC总成本：', total_cost, '$')
print('当前总收益：', current_total_profit, '$')
print('当前总收益率：', current_total_return, '%')

# 使用直方图查看收益率的稳定性
CFX_df['profit'].hist(bins=100)
plt.title('BTC Profit')
plt.show()
