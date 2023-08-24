from tradingview_ta import TA_Handler, Interval, Exchange, TradingView
import time

def readSymbols():
    sym = open("symbols.txt", "r")
    return sym.readlines()


if __name__ == "__main__":

    totalDict = {}
    bir = TA_Handler(
        symbol="",
        screener="Turkey",
        exchange="BIST",
        interval=Interval.INTERVAL_5_MINUTES
    )
    with open('symbols.txt') as f:
        symbols = f.readline().strip()
    lines = symbols.split(',')

    for l in lines:
        bir.symbol = l
        totalDict[l] = bir.get_analysis().indicators.get("RSI")
        #print("RSI FOR : ", l, " => ", bir.get_analysis().indicators.get("RSI"))
        #print("ANALYSIS", bir.get_analysis().summary)
    print("-----------------------------------------------------------------")
    sortedTotal = sorted(totalDict.items(), key=lambda x: x[1])
    for key, value  in sortedTotal:
        print ("RSI FOR: ", key, "=>", value)
    print("-----------------------------------------------------------------")
# print( TradingView.indicators )
# print ( bir.get_analysis().moving_averages)
# print ( bir.get_analysis().oscillators)
# print ( bir.get_analysis().indicators)
