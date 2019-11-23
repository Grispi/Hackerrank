import math
import os
import random
import re
import sys


def convertToBinary(n):
    binaryNumber = []
    i = 0
    while n > 0:
        if n % 2 == 0:
            binaryNumber.append("0")
        else:
            binaryNumber.append("1")
        i += 1
        n = (n//2)
    reverseList = list(reversed(binaryNumber))
    binaryNumber = int(''.join(reverseList))
    return binaryNumber


def convertToDecimal(n):
    decimalNumber = 0
    listNumber = list(reversed(str(n)))
    for x in range(0, len(listNumber)):
        decimalNumber = decimalNumber + (int(listNumber[x])*(2**x))

    return decimalNumber


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nk = input().split()
        n = int(nk[0])
        k = int(nk[1])

        listNumberN = []
        for j in range(1, n+1):
            listNumberN.append(j)

        resultDecimal = []
        for a in range(len(listNumberN)):
            for b in range(a+1, len(listNumberN)):
                letterA = listNumberN[a]
                letterB = listNumberN[b]
                # result2 = letterA & letterB
                # print("esto es binarioo??", result2)
                # resultDecimal.append(result2)

                result = convertToBinary(letterA) & convertToBinary(letterB)

                resultDecimal.append(convertToDecimal(result))

        values = (resultDecimal)

        max = 0
        listOfValues = []
        for value in values:
            value = int(value)
            if value > max and value < k:
                max = value
        print(max)
        #         break
        #     else int(value) < k:
        #         listOfValues.append(int(values[i]))
        # listOfValues.sort(reverse=True)
        # print(listOfValues[0])

    # for a in reversed(range(len(listNumberN))):
    #         for b in reversed(range(a+1, len(listNumberN))):
    #             letterA = listNumberN[a]
    #             letterB = listNumberN[b]
    #             result2 = letterA & letterB
    #             if result2 > max and result2 < k :
    #                 max = result2
    #                 if max == k-1:
    #                     break

    #     print(max)

    """
    Solution:

for _ in range(int(input())):
    n, k = map(int, input().split())
    a = k - 1
    b = ~a & -~a
    if a | b > n:
        print( a - 1)
    else:
        print (a)
        """

    """

Objective 
Welcome to the last day! Today, we're discussing bitwise operations. Check out the Tutorial tab for learning materials and an instructional video!

Task 
Given set . Find two integers,  and  (where ), from set  such that the value of  is the maximum possible and also less than a given integer, . In this case,  represents the bitwise AND operator.

Input Format

The first line contains an integer, , the number of test cases. 
Each of the  subsequent lines defines a test case as  space-separated integers,  and , respectively.

Constraints

Output Format

For each test case, print the maximum possible value of  on a new line.

Sample Input

3
5 2
8 5
2 2
Sample Output

1
4
0
Explanation



All possible values of  and  are:

The maximum possible value of  that is also  is , so we print  on a new line.
"""
