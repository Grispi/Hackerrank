import unittest
import sys


class Solution:

    def run(self, N, M):
        #
        # Some work here; return type and arguments should be according to the problem's requirements
        #
        new_list = []
        for i in range(N, M + 1):
            new_list.append(i)
        sequence = []
        for x in new_list:
            if (x % 3 == 0) and (x % 5 == 0):
                sequence.append('FizzBuzz')
            else:
                if x % 3 == 0:
                    sequence.append('Fizz')

                elif x % 5 == 0:
                    sequence.append('Buzz')

                else:
                    sequence.append(str(x))

        print(*(sequence), sep=", ")

        return ','.join(sequence)


so = Solution()
# n =int(input())
# m=int(input())
so.run(1, 5)


class SolutionMethods(unittest.TestCase):
    ##
    # /!\ Unit Tests are optional but highly recommended /!\
    ##
    # First Example
    ##
    # def test_example(self):
    #	self.assertEqual("this is an example", "this is an example")

    ##
    # Second Example
    ##
    def test_run(self):
        solution = Solution()
        self.assertEqual(solution.run(1, 5), "1,2,Fizz,4,Buzz")

    def test_run2(self):
        solution = Solution()
        self.assertEqual(solution.run(10, 15), "Buzz,11,Fizz,13,14,FizzBuzz")


if __name__ == "__main__":
    unittest.main()


"""Requirement
Write a program that returns the numbers from N to M both inclusive. But for multiples of three give "Fizz" instead of the number and for the multiples of five give "Buzz". For numbers which are multiples of both three and five, give "FizzBuzz".


INPUT 
int    N
Int    M


OUTPUT
string    sequence
^^ the resulting sequence using commas as separators between elements


EXAMPLE
Input
1,5
Output
"1,2,Fizz,4,Buzz"

  
  """
