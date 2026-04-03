from src.broker.base import BrokerBase
from src.simulator.trade import Trade


class SimBroker(BrokerBase):
    def __init__(self):
        self.open_trade = None
        self.trade_history = []
    
    def place_order(self, direction, entry_price, stop_loss, take_profit, timestamp):
        if self.open_trade is not None:
            return None  # already in a trade

            trade = Trade(
            direction=direction,
            entry_price=entry_price,
            stop_loss=stop_loss,
            take_profit=take_profit,
            entry_time=timestamp
            )

            self.open_trade = trade
        return trade

    def get_open_position(self):
        return self.open_trade

    def close_position(self, exit_price, timestamp):
        if self.open_trade is None:
            return None

            trade = self.open_trade

            trade.exit_price = exit_price
            trade.exit_time = timestamp
            trade.status = "closed"

            risk = abs(trade.entry_price - trade.stop_loss)

        if trade.direction == "long":
            trade.profit_r = (exit_price - trade.entry_price) / risk
        else:
            trade.profit_r = (trade.entry_price - exit_price) / risk

        trade.result = "win" if trade.profit_r > 0 else "loss"

        self.trade_history.append(trade)
        self.open_trade = None

        return trade