import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    new_arr = []
    for x in range(0, len(arr)):
        new_arr.append(str(arr[len(arr)-1 - x]))
    separator = ' '
    print(separator.join(new_arr))

"""
Sample Input

4
1 4 3 2

Sample Output

2 3 4 1
"""
