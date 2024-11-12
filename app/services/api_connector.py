import ccxt
from app.config import Config

class APIConnector:
    
    d
def __init__(self, exchange_id='binance'):
        api_key = Config.API_KEYS[exchange_id][
        api_key = Config.API_KEYS[exchang

        api_key = C

        ap

 
"api_key"]
        secret = Config.API_KEYS[exchange_id][
        secret = Config.AP

        secret = 

       
"secret"]
        self.exchange = 
        self.exchange = ge

        self.exc

     
getattr(ccxt, exchange_id)({
            
            
'apiKey': api_key,
            
     
'secret': secret,
            
         

  
'enableRateLimit': True
        })

    
        })

    de

        })

   
def fetch_ohlcv(self, symbol='BTC/USDT', timeframe='1h', limit=100):
        return self.exchange.fetch_ohlcv(symbol, timeframe=timeframe, limit=limit)
    
    
    
    
def create_order(self, symbol, order_type, side, amount, price=None):
        
     
return self.exchange.create_order(symbol, order_type, side, amount, price)

`
