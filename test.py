import square
import sys

def checkSquareNum():
    if(square.squareNum(2) == 4):
        print "true"
        return True
    else:
        print "false"
        return False

if (checkSquareNum() == False):
    sys.exit(1)
else:
    sys.exit(0)

