import random


def generate_number(min, max):
    """
    Generates a random integer between the specified minimum and maximum values.
    """
    min = int(min)
    max = int(max)
    return random.randint(min, max)


def generate_operator(): 
    """
    Generates a random arithmetic operator among +, -, and *.
    """
    return random.choice(['+', '-', '*'])


def perform_operation(number1, number2, operator):
    """
   Reads the equation and performs the operations based on the operator provided. 
   Returns the equation string and the result of the operation.
    """
    p = f"{number1} {operator} {number2}"
    if operator == '+': a = number1 + number2
    elif operator == '-': a = number1 - number2
    else: a = number1 * number2
    return p, a

def math_quiz():
    """
    Runs a math quiz game by generating random math problems and evaluating user answers.
    The user is presented with equations and asked to solve them.
    """
    s = 0
    total_questions = 5

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    # Loop through the total number of questions
    for _ in range(total_questions):

        # Generate random numbers and operator for the equation
        number1 = generate_number(1, 10); number2 = generate_number(1, 10); operator = generate_operator()

        # Generate the equation and calculate the correct answer
        problem, answer = perform_operation(number1, number2, operator)
        print(f"\nQuestion: {problem}")
        useranswer = input("Your answer: ")
        useranswer = int(useranswer)

        # Check user's answer and update the score
        if useranswer == answer:
            print("Correct! You earned a point.")
            s += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {answer}.")

    print(f"\nGame over! Your score is: {s}/{total_questions}")

if __name__ == "__main__":
    math_quiz()