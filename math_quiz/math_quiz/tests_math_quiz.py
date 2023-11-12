import unittest
from math_quiz import generate_number, generate_operator, perform_operation


class TestMathGame(unittest.TestCase):

    def test_generate_number(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generate_number(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_generate_operator(self):
        # Run the function to get an operator
        operator = generate_operator()
        
        # Define the valid operators
        valid_operators = {'+', '-', '*'}
        
        # Check if the generated operator is in the valid_operators set
        self.assertIn(operator, valid_operators, f"Generated operator '{operator}' is not valid.")
        pass

    def test_perform_operation(self):
            test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (8, 3, '-', '8 - 3', 5),
            (4, 6, '*', '4 * 6', 24)
            # Add more test cases as needed
        ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                # Run the function
                equation, result = perform_operation(num1, num2, operator)

                # Check the output
                self.assertEqual((equation, result), (expected_problem, expected_answer), f"Test failed for {num1} {operator} {num2}")

                pass

if __name__ == "__main__":
    unittest.main()
