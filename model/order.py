from os import pardir
from peewee import *
from .sqlite import db, BaseModel

# {
#     "clientOrderId": "testOrder", // 用户自定义的订单号
#     "cumQty": "0",
#     "cumQuote": "0", // 成交金额
#     "executedQty": "0", // 成交量
#     "orderId": 22542179, // 系统订单号
#     "avgPrice": "0.00000",  // 平均成交价
#     "origQty": "10", // 原始委托数量
#     "price": "0", // 委托价格
#     "reduceOnly": false, // 仅减仓
#     "side": "SELL", // 买卖方向
#     "positionSide": "SHORT", // 持仓方向
#     "status": "NEW", // 订单状态
#     "stopPrice": "0", // 触发价，对`TRAILING_STOP_MARKET`无效
#     "closePosition": false,   // 是否条件全平仓
#     "symbol": "BTCUSDT", // 交易对
#     "timeInForce": "GTC", // 有效方法
#     "type": "TRAILING_STOP_MARKET", // 订单类型
#     "origType": "TRAILING_STOP_MARKET",  // 触发前订单类型
#     "activatePrice": "9020", // 跟踪止损激活价格, 仅`TRAILING_STOP_MARKET` 订单返回此字段
#     "priceRate": "0.3", // 跟踪止损回调比例, 仅`TRAILING_STOP_MARKET` 订单返回此字段
#     "updateTime": 1566818724722, // 更新时间
#     "workingType": "CONTRACT_PRICE", // 条件价格触发类型
#     "priceProtect": false            // 是否开启条件单触发保护
# }


# Type	强制要求的参数
# LIMIT	timeInForce, quantity, price
# MARKET	quantity
# STOP, TAKE_PROFIT	quantity, price, stopPrice
# STOP_MARKET, TAKE_PROFIT_MARKET	stopPrice
# TRAILING_STOP_MARKET	callbackRate

# MARKET 市价单
# LIMIT 限价单
# STOP 止损单
# TAKE_PROFIT 止盈单
# LIQUIDATION 强平单

# 条件单的触发必须:

# 如果订单参数priceProtect为true:
# 达到触发价时，MARK_PRICE(标记价格)与CONTRACT_PRICE(合约最新价)之间的价差不能超过改symbol触发保护阈值
# 触发保护阈值请参考接口GET /fapi/v1/exchangeInfo 返回内容相应symbol中"triggerProtect"字段
# STOP, STOP_MARKET 止损单:
# 买入: 最新合约价格/标记价格高于等于触发价stopPrice
# 卖出: 最新合约价格/标记价格低于等于触发价stopPrice
# TAKE_PROFIT, TAKE_PROFIT_MARKET 止盈单:
# 买入: 最新合约价格/标记价格低于等于触发价stopPrice
# 卖出: 最新合约价格/标记价格高于等于触发价stopPrice
# TRAILING_STOP_MARKET 跟踪止损单:
# 买入: 当合约价格/标记价格区间最低价格低于激活价格activationPrice,且最新合约价格/标记价高于等于最低价设定回调幅度。
# 卖出: 当合约价格/标记价格区间最高价格高于激活价格activationPrice,且最新合约价格/标记价低于等于最高价设定回调幅度。
# TRAILING_STOP_MARKET 跟踪止损单如果遇到报错 {"code": -2021, "msg": "Order would immediately trigger."}
# 表示订单不满足以下条件:

# 买入: 指定的activationPrice 必须小于 latest price
# 卖出: 指定的activationPrice 必须大于 latest price
# newOrderRespType 如果传 RESULT:

# MARKET 订单将直接返回成交结果；
# 配合使用特殊 timeInForce 的 LIMIT 订单将直接返回成交或过期拒绝结果。
# STOP_MARKET, TAKE_PROFIT_MARKET 配合 closePosition=true:

# 条件单触发依照上述条件单触发逻辑
# 条件触发后，平掉当时持有所有多头仓位(若为卖单)或当时持有所有空头仓位(若为买单)
# 不支持 quantity 参数
# 自带只平仓属性，不支持reduceOnly参数
# 双开模式下,LONG方向上不支持BUY; SHORT 方向上不支持SELL
import datetime
from my_config import config


class Order(BaseModel):
    id = AutoField(primary_key=True)

    start_time = CharField()
    # SELL 卖 BUY 买
    side = CharField()
    # 未成交 成交  0   1    2
    state = IntegerField()
    # 币种
    pair = CharField()

    def set(self, side, state=0, start_time=''):
        self.create(side=side, state=state,
                    pair=config.pair, start_time=start_time)
        return

    class Meta:
        order_by = "id"
        db_table = 'order'


# Order.create_table()
