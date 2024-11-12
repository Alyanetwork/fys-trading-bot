from fastapi import FastAPI
from app.services.api_connector import APIConnector
from app.services.bots import DCABot, GridBot
from app.services.wallet_manager import WalletManager

app = FastAPI()
exchange = APIConnector()
wallet_manager = WalletManager()

@app.get("/trade/dca/")
def execute_dca(symbol: str, investment_amount: float, interval_hours: int):
    bot = DCABot(exchange, symbol, investment_amount, interval_hours)
    result = bot.execute()
    return {"status": "DCA order placed", "result": result}

@app.get("/wallet/")
def get_wallet_balance():
    return wallet_manager.get_balance()
