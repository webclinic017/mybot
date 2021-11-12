
# "feeTier": 0,  // 手续费等级
# "canTrade": true,  // 是否可以交易
# "canDeposit": true,  // 是否可以入金
# "canWithdraw": true, // 是否可以出金
# "updateTime": 0,
# "totalInitialMargin": "0.00000000",  // 但前所需起始保证金总额(存在逐仓请忽略), 仅计算usdt资产
# "totalMaintMargin": "0.00000000",  // 维持保证金总额, 仅计算usdt资产
# "totalWalletBalance": "23.72469206",   // 账户总余额, 仅计算usdt资产
# "totalUnrealizedProfit": "0.00000000",  // 持仓未实现盈亏总额, 仅计算usdt资产
# "totalMarginBalance": "23.72469206",  // 保证金总余额, 仅计算usdt资产
# "totalPositionInitialMargin": "0.00000000",  // 持仓所需起始保证金(基于最新标记价格), 仅计算usdt资产
# "totalOpenOrderInitialMargin": "0.00000000",  // 当前挂单所需起始保证金(基于最新标记价格), 仅计算usdt资产
# "totalCrossWalletBalance": "23.72469206",  // 全仓账户余额, 仅计算usdt资产
# "totalCrossUnPnl": "0.00000000",    // 全仓持仓未实现盈亏总额, 仅计算usdt资产
# "availableBalance": "23.72469206",       // 可用余额, 仅计算usdt资产
# "maxWithdrawAmount": "23.72469206"     // 最大可转出余额, 仅计算usdt资产
from my_config import config


class account(object):

    #  账户总余额 模拟环境不默认为 0
    totalWalletBalance = 0.0
    # 可用余额
    availableBalance = 0.0


class Meta:
    db_table = 'account'
