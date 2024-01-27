#/usr/bin/env python3
import sys


def primef(n):
    if n <= 3:
        return int(n)
    if n % 2 == 0:
        return 2
    elif n % 3 == 0:
        return 3
    else:
        for pipox in range(5, int((n)**0.5) + 1, 6):
            if n % pipox == 0:
                return int(pipox)
            if n % (pipox + 2) == 0:
                return primef(n/(pipox+2))
    return int(n)


print(primef(int(sys.argv[1])))
