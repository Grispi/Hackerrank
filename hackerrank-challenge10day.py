import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input())
    result = []
    i = 0
    while n > 0:
        if n % 2 == 0:
            result.append(0)
        else:
            result.append(1)
        i += 1
        n = (n//2)
        print(n)

    reverseList = list(reversed(result))
    count = 0
    countBigger = 0
    for x in range(0, len(reverseList)):
        if reverseList[x] == 1:
            count += 1

            #print(count, reverseList[2], x, len(reverseList))

            if countBigger < count:
                countBigger = count
        elif reverseList[x] == 0:
            count = 0
    print(countBigger)

"""
Objective 
Today, we're working with binary numbers. Check out the Tutorial tab for learning materials and an instructional video!

Task 
Given a base- integer, , convert it to binary (base-). Then find and print the base- integer denoting the maximum number of consecutive 's in 's binary representation.

Input Format

A single integer, .

Constraints

Output Format

Print a single base- integer denoting the maximum number of consecutive 's in the binary representation of .

Sample Input 1

5
Sample Output 1

1
Sample Input 2

13
Sample Output 2

2
Explanation

Sample Case 1: 
The binary representation of  is , so the maximum number of consecutive 's is .

Sample Case 2: 
The binary representation of  is , so the maximum number of consecutive 's is .
"""
