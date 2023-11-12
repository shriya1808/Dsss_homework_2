import random


def choose_random_integer(min, max):
    """
    Args:
        min (int): lower bound
        max (int): upper bound

    Returns:
        (int) A Random integer between [min, max], including both points.
    """
    return random.randint(min, max)


def choose_random_operator():
    """
    Returns:
        (str) A Random operator '+', '-' or '*'.
    """
    return random.choice(['+', '-', '*'])


def get_question_and_answer(n1, n2, o):
    """
    Args:
        n1 (int): left operand
        n1 (int): right operand
        o (str): operator

    Returns:
        question (str): the question to be solved by the user.
        answer (int): answer for the question.
    """
    question = f"{n1} {o} {n2}"

    # if-else condition checks for which operation to be performed
    if o == '+': answer = n1 + n2
    elif o == '-': answer = n1 - n2
    else: answer = n1 * n2

    return question, answer

def math_quiz():
    """
    Conducts the Math Quiz Game by generating 5 questions and awards user 1 point for each correct answer.
    """

    score = 0  # points scored by the user is set to 0 initially
    ques = 5    # number of questions in Quiz

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(ques):
        # choosing random operands and operator
        n1 = choose_random_integer(1, 10)
        n2 = choose_random_integer(1, 5)
        o = choose_random_operator()

        # get Question and its answer
        question, answer = get_question_and_answer(n1, n2, o)

        # print question and get user answer
        print(f"\nQuestion: {question}")
        try:
            useranswer = input("Your answer: ")
            useranswer = int(useranswer)
        except:
            print("Invalid Input, value must be an integer.")
            print(f"The correct answer is {answer}.")
            continue

        # check user answer
        if useranswer == answer:
            print("Correct! You earned a point.")
            score += 1   # award 1 point to correct answer
        else:
            print(f"Wrong answer. The correct answer is {answer}.")

    print(f"\nGame over! Your score is: {score}/{ques}")

if __name__ == "__main__":
    math_quiz()
