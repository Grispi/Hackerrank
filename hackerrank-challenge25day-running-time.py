# import math
# T = int(input())
# for i in range(T):
#     number = int(input())
#     prime = True
#     if number == 1:
#         prime = False
#     elif number <= 5 and number != 4:
#         prime = True

#     elif number % 2 == 0 or number % 3 == 0 or number % 5 == 0:
#         prime = False
#     else:
#         divisor = math.ceil(number/2)
#         while divisor > 1:
#             if number % divisor == 0:
#                 prime = False
#                 break
#             else:
#                 divisor = divisor - 1
#                 prime = True

#     if prime:
#         print("Prime")
#     else:
#         print("Not prime")


import math

T = int(input())
for i in range(T):
    number = int(input())
    prime = True
    if number == 2:
        prime = True

    elif number == 1 or (number & 1) == 0:
        prime = False

    else:
        for i in range(2, math.ceil(math.sqrt(number)) + 1):
            if (number % i) == 0:
                prime = False
                break

    if prime:
        print("Prime")
    else:
        print("Not prime")

"""
Objective 
Today we're learning about running time! Check out the Tutorial tab for learning materials and an instructional video!

Task 
A prime is a natural number greater than  that has no positive divisors other than  and itself. Given a number, , determine and print whether it's  or .

Note: If possible, try to come up with a  primality algorithm, or see what sort of optimizations you come up with for an  algorithm. Be sure to check out the Editorial after submitting your code!

Input Format

The first line contains an integer, , the number of test cases. 
Each of the  subsequent lines contains an integer, , to be tested for primality.

Constraints

Output Format

For each test case, print whether  is  or  on a new line.

Sample Input

3
12
5
7
Sample Output

Not prime
Prime
Prime
Explanation

Test Case 0: . 
 is divisible by numbers other than  and itself (i.e.: , , ), so we print  on a new line.

Test Case 1: . 
 is only divisible  and itself, so we print  on a new line.

Test Case 2: . 
 is only divisible  and itself, so we print  on a new line.
 """
"""
Editorial
import math

def isPrime(n):
    if n == 2:
        return True
    elif n == 1 or (n & 1) == 0:
        return False
        
    for i in range(2, math.ceil(math.sqrt(n)) + 1):
        if (n % i) == 0:
            return False
    
    return True

p = int(input())
for i in range(0, p):
    x = int(input())

    s = "Prime" if (isPrime(x)) else "Not prime"
    print(s);
"""
