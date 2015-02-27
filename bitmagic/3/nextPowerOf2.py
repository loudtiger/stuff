import math
import sys

inputValue = sys.argv[1]

lg = math.log(int(inputValue), 2)
print str(int(math.pow(2, math.ceil(lg))))
