#/usr/bin/env python3
import sys


def primef(pipox):
    if pipox <= 3:
        return int(pipox)
    if pipox % 2 == 0:
        return 2
    elif pipox % 3 == 0:
        return 3
    else:
        for i in range(5, int((pipox)**0.5) + 1, 6):
            if pipox % i == 0:
                return int(i)
            if pipox % (i + 2) == 0:
                return primef(pipox/(i+2))
    return int(pipox)


print(primef(int(sys.argv[1])))
