# Enter your code here. Read input from STDIN. Print output to STDOUT

actualDate = list(map(int, input().rstrip().split()))
expectedDate = list(map(int, input().rstrip().split()))


def calculateFine(actualDate, expectedDate):
    dayADate, monthADate, yearADate = actualDate[0], actualDate[1], actualDate[2]
    dayEDate, monthEDate, yearEDate = expectedDate[0], expectedDate[1], expectedDate[2]
    # if (dayADate <= dayEDate) and monthADate <= monthEDate and yearADate <= yearEDate:
    #     print("0")
    # elif(dayADate > dayEDate)and monthADate == monthEDate and yearADate == yearEDate:
    #     daysLate = dayADate - dayEDate
    #     fine = 15 * int(daysLate)
    #     print(fine)
    # elif monthADate != monthEDate and yearADate == yearEDate:
    #     monthsLate = monthADate - monthEDate
    #     fine = 500 * int(monthsLate)
    #     print(fine)
    # else:
    #     print("10000")
    if yearADate < yearEDate:
        print('0')
    elif yearADate == yearEDate:
        if monthADate < monthEDate:
            print('0')
        elif monthADate == monthEDate:
            if dayADate <= dayEDate:
                print('0')
            else:
                daysLate = dayADate - dayEDate
                fine = 15 * int(daysLate)
                print(fine)
        else:
            monthsLate = monthADate - monthEDate
            fine = 500 * int(monthsLate)
            print(fine)
    else:
        print("10000")


calculateFine(actualDate, expectedDate)

"""
Objective 
Today's challenge puts your understanding of nested conditional statements to the test. You already have the knowledge to complete this challenge, but check out the Tutorial tab for a video on testing!

Task 
Your local library needs your help! Given the expected and actual return dates for a library book, create a program that calculates the fine (if any). The fee structure is as follows:

If the book is returned on or before the expected return date, no fine will be charged (i.e.: .
If the book is returned after the expected return day but still within the same calendar month and year as the expected return date, .
If the book is returned after the expected return month but still within the same calendar year as the expected return date, the .
If the book is returned after the calendar year in which it was expected, there is a fixed fine of .
Input Format

The first line contains  space-separated integers denoting the respective , , and  on which the book was actually returned. 
The second line contains  space-separated integers denoting the respective , , and  on which the book was expected to be returned (due date).

Constraints

Output Format

Print a single integer denoting the library fine for the book received as input.

Sample Input

9 6 2015
6 6 2015
Sample Output

45
Explanation

Given the following return dates: 
Actual:  
Expected: 

Because , we know it is less than a year late. 
Because , we know it's less than a month late. 
Because , we know that it was returned late (but still within the same month and year).

Per the library's fee structure, we know that our fine will be . We then print the result of  as our output.
"""
