import unittest
from math_quiz import choose_random_integer, choose_random_operator, get_question_and_answer


class TestMathGame(unittest.TestCase):

    def test_function_choose_random_integer(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = choose_random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_function_choose_random_operator(self):
        # Test if operator generated is '+', '-' or '*'
        operators = ['+', '-', '*']
        for _ in range(1000):  # Test large number of times
            rand_operator = choose_random_operator()
            self.assertIn(rand_operator, operators)

    def test_function_get_question_and_answer(self):
        # Test if questions and answers generated are correct

        # test case format (left operand, right operand, operator, expected_problem, expected_answer)
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (6, 1, '-', '6 - 1', 5),
            (9, 4, '*', '9 * 4', 36),
            (-6, 1, '+', '-6 + 1', -5),
            (2, 3, '-', '2 - 3', -1),
            (-1,-5, '*', '-1 * -5', 5),
            (-1, 1, '*', '-1 * 1', -1)
        ]

        # check if generated problem & answer matches to the expected problem & answer for each test case
        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            generated_problem, generated_answer = get_question_and_answer(num1, num2, operator)
            self.assertListEqual([generated_problem, generated_answer], [expected_problem, expected_answer])

if __name__ == "__main__":
    unittest.main()
