import talib
import numpy as np

class Indicators:
    @staticmethod
    def calculate_rsi(data, period=14):
        return talib.RSI(np.array(data['close']), timeperiod=period)
    
    @staticmethod
    def calculate_macd(data, fast_period=12, slow_period=26, signal_period=9):
        macd, macdsignal, macdhist = talib.MACD(np.array(data['close']), fastperiod=fast_period, slowperiod=slow_period, signalperiod=signal_period)
        return macd, macdsignal, macdhist
