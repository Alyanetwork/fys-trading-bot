import ccxt

class APIConnector:
    def __init__(self, exchange_id='binance'):
        api_key = Config.API_KEYS[exchange_id]["api_key"]
        secret = Config.API_KEYS[exchange_id]["secret"]
        self.exchange = getattr(ccxt, exchange_id)({
            'apiKey': api_key,
            'secret': secret,
            'enableRateLimit': True
        })

    def fetch_ohlcv(self, symbol='BTC/USDT', timeframe='1h', limit=100):
        return self.exchange.fetch_ohlcv(symbol, timeframe=timeframe, limit=limit)
    
    def create_order(self, symbol, order_type, side, amount, price=None):
        return self.exchange.create_order(symbol, order_type, side, amount, price)
