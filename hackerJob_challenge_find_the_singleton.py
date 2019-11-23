import unittest


class Solution:

    def run(self, student_list):
        #
        # Some work here; return type and arguments should be according to the problem's requirements
        #
        single_student = None
        dicc = {}

        for student in student_list:
            if student in dicc:
                dicc[student] += 1
            else:
                dicc[student] = 1
        for student, number in dicc.items():
            if number == 1:
                single_student = student

        single_student_number = single_student
        return single_student_number


class SolutionMethods(unittest.TestCase):
        ##
        # /!\ Unit Tests are optional but highly recommended /!\
        ##
        # First Example
        ##
        # def test_example(self):
        # 	self.assertEqual("this is an example", "this is an example")

        ##
        # Second Example
        ##
    def test_run(self):
        solution = Solution()
        self.assertEqual(solution.run([2, 4, 5, 4, 2]), 5)

    def test_run(self):
        solution = Solution()
        self.assertEqual(solution.run(
            [2, 4, 5, 4, 2, 5, 25, 25, 50, 50, 80]), 80)


if __name__ == "__main__":
    unittest.main()
