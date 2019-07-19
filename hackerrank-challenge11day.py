#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the hourglassSum function below.


def hourglassSum(arr):
    total2 = 0
    total = -63
    for i in range(4):
        for x in range(4):
            total2 = arr[i][0+x]+arr[i][1+x]+arr[i][2+x] + \
                arr[1+i][1+x] + arr[2+i][x]+arr[2+i][1+x]+arr[2+i][2+x]
            if total2 > total:
                total = total2

    return total


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)
    print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()

# input:
# 1 1 1 0 0 0
# 0 1 0 0 0 0
# 1 1 1 0 0 0
# 0 0 2 4 4 0
# 0 0 0 2 0 0
# 0 0 1 2 4 0
# output:19
# buscar la suma mayor del reloj de arena abc/d/efc
# input:
# -1 -1 0 -9 -2 -2
# -2 -1 -6 -8 -2 -5
# -1 -1 -1 -2 -3 -4
# -1 -9 -2 -4 -4 -5
# -7 -3 -3 -2 -9 -9
# -1 -3 -1 -2 -4 -5
# output:
# -6
