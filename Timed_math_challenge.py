import random

#Constants that dont change in CAPS
OPERATOR =["+", "-", "*"]
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 10

def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATOR)

    expr = str(left) + " " + operator + " " + str(right)
    answer = eval(expr)
    return expr , answer

for i in range(TOTAL_PROBLEMS):
    expr, answer = generate_problem()
    while True:
        guess = input("Problem #" + str(i + 1) + ":" + expr + " = ") 
        if guess == str(answer):
            break
