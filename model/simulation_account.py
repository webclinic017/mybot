from my_config import config


class simulation_account(object):
    # 可用余额
    availableBalance = 0.0

    def __init__(self, *args):
        self.availableBalance = config.balance
        return
