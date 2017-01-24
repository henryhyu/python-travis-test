import square
import sys

def checkSquareNum():
    if(square.squareNum(1) == 4):
        print "true"
        return True
    else:
        print "false"
        return False

if (checkSquareNum() == False):
    sys.exit(1)

