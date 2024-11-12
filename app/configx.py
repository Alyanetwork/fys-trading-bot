import os

class Config:
    API_KEYS = {
        "binance": {
            "api_key": os.getenv("BINANCE_API_KEY"),
            "secret": os.getenv("BINANCE_SECRET_KEY"),
        }
        # Diğer borsaların API bilgileri buraya eklenebilir
    }
    DEFAULT_SYMBOL = 'BTC/USDT'
    DEFAULT_EXCHANGE = 'binance'
