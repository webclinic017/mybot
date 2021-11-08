机器人执行逻辑¶
以试运行或实时模式（使用freqtrade trade）启动 freqtrade将启动机器人并启动机器人迭代循环。默认情况下，循环每隔几秒 ( internals.process_throttle_secs)运行一次，并按以下顺序大致执行以下操作：

从持久性中获取未平仓交易。
计算当前可交易对的列表。
下载包含所有信息对的配对列表的 ohlcv 数据
此步骤每个 Candle 仅执行一次，以避免不必要的网络流量。
调用bot_loop_start()策略回调。
分析每对策略。
称呼 populate_indicators()
称呼 populate_buy_trend()
称呼 populate_sell_trend()
检查未结订单的超时时间。
调用check_buy_timeout()未结买单的策略回调。
调用check_sell_timeout()未结卖单的策略回调。
验证现有头寸并最终下卖单。
考虑止损、投资回报率和卖出信号，custom_sell()以及custom_stoploss()。
根据ask_strategy配置设置或使用custom_exit_price()回调确定卖出价格。
在下卖单之前，confirm_trade_exit()调用策略回调。
检查交易槽是否仍然可用（如果max_open_trades已达到）。
验证尝试进入新头寸的买入信号。
根据bid_strategy配置设置或使用custom_entry_price()回调确定买入价格。
通过调用custom_stake_amount()回调确定赌注大小。
在下达买单之前，confirm_trade_entry()调用策略回调。
这个循环会一次又一次地重复，直到机器人停止。

