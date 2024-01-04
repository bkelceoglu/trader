from tradingview_ta import TA_Handler, Interval
import os
from typing import (
    Any,
    List,
)
from cmd2 import ansi
from cmd2.table_creator import  SimpleTable, Column

import Utils

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Services():
    target = TA_Handler(
        symbol="",
        screener="Turkey",
        exchange="BIST",
        interval=Interval.INTERVAL_1_HOUR
    )

    dataList : List[List[Any]] = list()
    columns : List[Column] = list()

    def __int__(self):
        pass

    def setInterval(argument):
        if argument == "1H":
            Services.target.interval = Interval.INTERVAL_1_HOUR
        elif argument == "5M":
            Services.target.interval = Interval.INTERVAL_5_MINUTES
        elif argument == "1D":
            Services.target.interval = Interval.INTERVAL_1_DAY
        else:
            print( "No such value to set..." )
        Services.interval()

    def interval():
        print ("interval set to: ", Services.target.interval)

    def getRSI(symbol):
        Services.target.symbol = symbol.rstrip()
        try:
            return Services.target.get_analysis().indicators.get("RSI")
        except:
            pass

    def getOpenPrice(sym):
        Services.target.symbol = sym.rstrip()
        return Services.target.get_analysis().indicators.get("open")
    def getLowPrice(symbol):
        Services.target.symbol = symbol.rstrip()
        return Services.target.get_analysis().indicators.get("low")

    def getHighPrice (sym):
        Services.target.symbol = sym.rstrip()
        return Services.target.get_analysis().indicators.get("high")
    def getPriceAndDiffs(symbol):
        Services.target.symbol = symbol.rstrip()
        try:
            open_price = Services.getOpenPrice(Services.target.symbol)
            low = Services.getLowPrice(Services.target.symbol)
            high = Services.getHighPrice(Services.target.symbol)
            diff = high - low
            retstr = "open price:\t\t" + str(open_price) + "\nlow price:\t\t" + str(low) + "\nhigh price:\t\t" + str(high) + "\ndifferencial:\t\t" + str(diff)
            return retstr
        except:
            pass

    def getPriceAndDiffTable(symbol):
        Services.interval()
        Services.target.symbol = symbol.rstrip()
        Services.columns.clear()
        Services.columns.append(Column ("Symbol", width = 10))
        Services.columns.append(Column ("Open Price", width=10))
        Services.columns.append(Column ("Low Price", width=10))
        Services.columns.append(Column ("High Price", width=10))
        Services.columns.append(Column ("Diff Price", width=10))
        Services.columns.append(Column ("RSI", width=10))
        Services.columns.append(Column ("RSI - D", width=10))
        Services.columns.append(Column ("RSI - K", width=10))
        Services.columns.append(Column ("RSI DIFF", width=10))
        Services.dataList.clear()
        simpleTable = SimpleTable(Services.columns)
        open_price = Services.getOpenPrice(Services.target.symbol)
        low = Services.getLowPrice(Services.target.symbol)
        high = Services.getHighPrice(Services.target.symbol)
        diff = high - low
        diff = round(diff, 2)
        rsi = round(Services.getRSI(symbol), 2)
        rsid = round(Services.target.get_analysis().indicators.get("Stoch.D"), 2)
        rsik = round(Services.target.get_analysis().indicators.get("Stoch.K"), 2)
        rsi_diff = round(rsid - rsik, 2)
        Services.dataList.append( [Services.target.symbol, open_price, low, high, diff, rsi, rsid, rsik, rsi_diff] )
        table = simpleTable.generate_table(Services.dataList)
        Utils.TablePrint.ansiPrint(table)


    def getFollowingSymbolsFiles(self):
        files = os.listdir("list/")
        return files
    def getAllFromFollowed(fileName):
        l = Utils.ReadList.readFollowingList(fileName)
        Services.columns.clear()
        Services.dataList.clear()
        Services.columns.append(Column ("Symbol", width = 10))
        Services.columns.append(Column ("Open Price", width=10))
        Services.columns.append(Column ("Low Price", width=10))
        Services.columns.append(Column ("High Price", width=10))
        Services.columns.append(Column ("Diff Price", width=10))
        Services.columns.append(Column ("Change", width=10))
        Services.columns.append(Column ("RSI", width=10))
        Services.columns.append(Column ("RSI - D", width=10))
        Services.columns.append(Column ("RSI - K", width=10))
        simpleTable = SimpleTable(Services.columns)
        for sym in l:
            Services.target.symbol = sym.rstrip()
            open_price = Services.getOpenPrice(Services.target.symbol)
            low = Services.getLowPrice(Services.target.symbol)
            high = Services.getHighPrice(Services.target.symbol)
            diff = high - low
            diff = round(diff, 2)
            change = round (Services.target.get_analysis().indicators.get("change"))
            rsi = round(Services.getRSI(Services.target.symbol), 2)
            rsid = round(Services.target.get_analysis().indicators.get("Stoch.D"), 2)
            rsik = round(Services.target.get_analysis().indicators.get("Stoch.K"), 2)
            Services.dataList.append( [Services.target.symbol, open_price, low, high, diff, change, rsi, rsid, rsik] )
        t = simpleTable.generate_table(Services.dataList)
        Utils.TablePrint.ansiPrint(t)

    def getFromFollowedNoTable (fileName):
        Services.interval()
        symbolList = Utils.ReadList.readFollowingList(fileName)
        print(f'{bcolors.BOLD}{"SYMBOL":<10}{"OPEN-PR":<10}{"LOW-PR":<10}{"HIGH-PR":<10}{"CHANGE":<10}{"RSI":<10}{"RSI-D":<10}{"RSI-K":<10}{"RSI-DIFF(K-D)":<10}{bcolors.ENDC}')
        print ('-'*100)
        for s in symbolList:
            Services.target.symbol = s.rstrip()
            open_price = Services.getOpenPrice(s)
            low = Services.getLowPrice(s)
            high = Services.getHighPrice(s)
            change = round (Services.target.get_analysis().indicators.get("change"),2)
            rsi = round( Services.getRSI(Services.target.symbol), 2 )
            rsid = round( Services.target.get_analysis().indicators.get("Stoch.D"), 2 )
            rsik = round( Services.target.get_analysis().indicators.get("Stoch.K"), 2 )
            rsi_diff = round (rsik - rsid, 2)
            if rsi_diff > 0:
                print( f'{bcolors.OKGREEN}{s.rstrip(): <10}{open_price: <10}{low: <10}{high: <10}{change: <10}{rsi: <10}{rsid: <10}{rsik: <10}{rsi_diff: <10}{bcolors.ENDC}' )
            else:
                print( f'{bcolors.FAIL}{s.rstrip(): <10}{open_price: <10}{low: <10}{high: <10}{change: <10}{rsi: <10}{rsid: <10}{rsik: <10}{rsi_diff: <10}{bcolors.ENDC}' )
        print ('-'*80)




