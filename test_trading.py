from app.services.api_connector import APIConnector
from app.services.bots import DCABot

def test_dca_bot():
    exchange = APIConnector()
    bot = DCABot(exchange, "BTC/USDT", 100, 1)
    result = bot.execute()
    assert result is not None, "DCA bot execution failed."
