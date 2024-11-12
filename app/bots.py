from datetime import datetime, timedelta

class DCABot:
    def __init__(self, exchange, symbol, investment_amount, interval_hours):
        self.exchange = exchange
        self.symbol = symbol
        self.investment_amount = investment_amount
        self.interval_hours = interval_hours
        self.last_investment_time = datetime.now() - timedelta(hours=interval_hours)

    def execute(self):
        if datetime.now() >= self.last_investment_time + timedelta(hours=self.interval_hours):
            order = self.exchange.create_order(self.symbol, 'market', 'buy', self.investment_amount)
            self.last_investment_time = datetime.now()
            return order

class GridBot:
    def __init__(self, exchange, symbol, grid_levels, grid_size):
        self.exchange = exchange
        self.symbol = symbol
        self.grid_levels = grid_levels
        self.grid_size = grid_size
        self.orders = []

    def create_grid(self):
        ticker = self.exchange.fetch_ticker(self.symbol)
        price = ticker['last']
        for i in range(self.grid_levels):
            level_price = price + (i - self.grid_levels // 2) * self.grid_size
            self.orders.append({'price': level_price, 'status': 'pending'})

    def execute(self):
        ticker = self.exchange.fetch_ticker(self.symbol)
        price = ticker['last']
        for order in self.orders:
            if order['status'] == 'pending' and abs(order['price'] - price) < self.grid_size / 2:
                self.exchange.create_order(self.symbol, 'limit', 'buy', 1, order['price'])
                order['status'] = 'filled'
