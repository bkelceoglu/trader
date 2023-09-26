import Services, Utils
from cmd2 import cmd2



from cmd2.table_creator import (SimpleTable,Column)
class CommandsAll(cmd2.Cmd):
    intro = 'Type help or ? to list commands.\n' + ' INTERVAL FOR ANALYSIS SET TO 1 HOUR \n'
    prompt = 'TA-1500>>>> '
    file = None

    def do_get_rsi_for (self, args):
        """ gives rsi for given symbol """
        res = Services.Services.getRSI(args)
        if res == None:
            print ( "No symbol found." )
        else:
            print ( "RSI: ", Services.Services.getRSI(args) )

    def do_set_interval(self, args):
        """ set interval for value gathering
                    valid values:
                    1H = 1 hour
                    5M = 5 minutes
                    1D = 1 day
        """
        Services.Services.setInterval(args)

    def do_open_price(self, args):
        """ gives opening price for given symbol """
        print(Services.Services.getOpenPrice(args))
    def do_low_price(self, args):
        """ gives low price for given symbol """
        print(Services.Services.getLowPrice(args))
    def do_high_price(self, args):
        """ gives high price for given symbol """
        print(Services.Services.getHighPrice(args))
    def do_prices_and_diffs(self, args):
        """ gives prices and differencials for given symbol """
        print ( Services.Services.getPriceAndDiffs(args) )
    def do_get_prices_for(self, args):
        """ get analysis for specific symbol """
        Services.Services.getPriceAndDiffTable(args)
    def do_get_following_files(self, args):
        """ returns following symbol files in list folder """
        print (Services.Services.getFollowingSymbolsFiles(self))

    def do_get_from_following(self, args):
        """ create table from given following file """
        #Services.Services.getAllFromFollowed(args)
        Services.Services.getFromFollowedNoTable(args)
