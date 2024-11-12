import talib
import numpy as np

class Indicators:
    @staticmethod
    def calculate_rsi(data, period=14):
        return talib.RSI(np.array(data['close']), timeperiod=period)
    
    @staticmethod
    def calculate_macd(data, fast_period=12, slow_period=26, signal_period=9):
        macd, macdsignal, macdhist = talib.MACD(
            np.array(data['close']), fastperiod=fast_period, 
            slowperiod=slow_period, signalperiod=signal_period)
        return macd, macdsignal, macdhist

    @staticmethod
    def calculate_bollinger_bands(data, period=20, std_dev=2):
        upperband, middleband, lowerband = talib.BBANDS(
            np.array(data['close']), timeperiod=period, 
            nbdevup=std_dev, nbdevdn=std_dev, matype=0)
        return upperband, middleband, lowerband

    @staticmethod
    def calculate_sma(data, period=30):
        return talib.SMA(np.array(data['close']), timeperiod=period)

    @staticmethod
    def calculate_ema(data, period=30):
        return talib.EMA(np.array(data['close']), timeperiod=period)
