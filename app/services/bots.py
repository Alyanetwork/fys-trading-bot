from datetime import datetime, timedelta



cla
class DCABot:
    
   
def __init__(self, exchange, symbol, investment_amount, interval_hours):
        self.exchange = exchange
        self.symbol = symbol
        self.investment_amount = investment_amount
        self.interval_hours = interval_hours
        self.last_investment_time = datetime.now() - timedelta(hours=interval_hours)

    
        self.exchange = exchange
        self.symbol = symbol
        self.investment_amount = investment_amount
        self.interval_hours = interval_hours
        self.last_investment_time = datetime.now() - timedelta(hours=interval_hours)


        self.exchange = exchange
        self.symbol = symbol
        self.investment_amount = investment_amount
        self.interval_hours = interval_hours
        self.last_investment_time = datetime.now() - timedelta(hours=interval_h

        self.exchange = exchange
        self.symbol = symbol
        self.investment_amount = investment_amount
        self.interval_hours = interval_hours
        self.last_investment_time = datetime.now() - timedelta(hours=
        self.exchange = exchange
        self.symbol = symbol
        self.investment_amount = investment_amount
        self.interval_hours = interval_hours
        self.last_investment_time = datetime.now() - timedelta

        self.exchange = exchange
        self.symbol = symbol
        self.investment_amount = investment_amount
        self.interval_hours = interval_hours
        self.last_investment_time = datetime.now() -

        self.exchange = exchange
        self.symbol = symbol
        self.investment_amount = investment_amount
        self.interval_hours = interval_hours
        self.last_investment_time = datet

        self.exchange = exchange
        self.symbol = symbol
        self.investment_amount = investment_amount
        self.interval_hours = interval_hours
        self.last_investment_

        self.exchange = exchange
        self.symbol = symbol
        self.investment_amount = investment_amount
        self.interval_hours = interval_hours
        self.la

        self.exchange = exchange
        self.symbol = symbol
        self.investment_amount = investment_amount
        self.interval_hours = interval_hours
      

        self.exchange = exchange
        self.symbol = symbol
        self.investment_amount = investment_amount
        self.interval_hours = interval_ho

        self.exchange = exchange
        self.symbol = symbol
        self.investment_amount = investment_amount
        self.interval_hours = 

        self.exchange = exchange
        self.symbol = symbol
        self.investment_amount = investment_amount
        self.inter

        self.exchange = exchange
        self.symbol = symbol
        self.investment_amount = investment_amou

        self.exchange = exchange
        self.symbol = symbol
        self.investment_amount = invest

        self.exchange = exchange
        self.symbol = symbol
        self.investment_amoun

        self.exchange = exchange
        self.symbol = symbol
        self.inves

        self.exchange = exchange
        self.symbol = symbol
      

        self.exchange = exchange
        self.

        self.exchange = exchange
    

        self.exchange = exc

        self.exc
def execute(self):
        if datetime.now() >= self.last_investment_time + timedelta(hours=self.interval_hours):
            order = self.exchange.create_order(self.symbol, 
            order = self.exchange.create_order(self.symb

            order = self.exchange.create_order(self.sy

            order = self.exchange.create_order(self

            order = self.exchange.create

      

   
'market', 'buy', self.investment_amount)
            self.last_investment_time = datetime.now()
            
            self.last_investment_time = datetime.now()
      

            self.last_investment_time = datetime.no

            self.last_investment_time = dateti

            self.last_investment_time = 

            self.last_investment_

            self.last_inve

            self.l
return order



clas
class GridBot:
    def __init__(self, exchange, symbol, grid_levels, grid_size):
        self.exchange = exchange
        self.symbol = symbol
        self.grid_levels = grid_levels
        self.grid_size = grid_size
        self.orders = []

    
        self.exchange = exchange
        self.symbol = symbol
        self.grid_levels = grid_levels
        self.grid_size = grid_size
        self.orders = []

    

        self.exchange = exchange
        self.symbol = symbol
        self.grid_levels = grid_levels
        self.grid_size = grid_size
        self.
        self.exchange = exchange
        self.symbol = symbol
        self.grid_levels = grid_levels
        self.grid_size = grid_size
       

        self.exchange = exchange
        self.symbol = symbol
        self.grid_levels = grid_levels
        self.grid_size = grid_si

        self.exchange = exchange
        self.symbol = symbol
        self.grid_levels = grid_levels
        self.grid_siz

        self.exchange = exchange
        self.symbol = symbol
        self.grid_levels = grid_l

        self.exchange = exchange
        self.symbol = symbol
        self.grid_levels 

        self.exchange = exchange
        self.symbol = symbol
        self.gri

        self.exchange = exchange
        self.symbol = symbol
      

        self.exchange = exchange
        self.symbol = sy

        self.exchange = exchange
        self

        self.exchange = exchange
     

        self.exchange = exchan

        self.exchange

        sel
def create_grid(self):
        ticker = self.exchange.fetch_ticker(self.symbol)
        price = ticker[
        ticker = self.exchange.fetch_ticker(self.symbol)
        price 

        ticker = self.exchange.fetch_ticker(self.symbol)
   

        ticker = self.exchange.fetch_ticker(self

        ticker = self.exchange.fetc

        tic

 
'last']
        for i in range(self.grid_levels):
            level_price = price + (i - self.grid_levels // 
            level_price = price + (i - self.grid_level

            level_price = price + (i - self.g

            level_price = price + (

          

  
2) * self.grid_size
            self.orders.append({
            self.orders.a

            sel
'price': level_price, 'status': 'pending'})

    def execute(self):
        ticker = self.exchange.fetch_ticker(self.symbol)
        price = ticker[
        ticker = self.exchange.fetch_ticker(self.symbol)
  

        ticker = self.exchange.fetch_ticker(self.

        ticker = self.exchange.fetch_t

        ticke

     
'last']
        
       
for order in self.orders:
            
            
if order['status'] == 'pending' and abs(order['price'] - price) < self.grid_size / 2:
                self.exchange.create_order(self.symbol, 
                self.exchange.create_order(self.sy

                self.exchange.create_order

                self.exchange.cre

                self.ex

     
'limit', 'buy', 1, order['price'])
                order[
                o

         
'status'] = 'filled'
