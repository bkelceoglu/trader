import sys
from cmd2 import ansi
from cmd2.table_creator import  SimpleTable


class TablePrint:
    def __init__(self):
        pass

    def ansiPrint(text: SimpleTable):
        ansi.style_aware_write(sys.stdout, text + "\n")


class ReadList:
    def __init__(self):
        pass

    def readFollowingList(fileName):
        with open("list/" + fileName, "r") as f:
            s = f.readlines()
            return s