import random
import itertools

operators = ['+', '-', '*', '/']

def generate_equation():
    a, b, c, d, e = random.randint(1, 9), random.randint(1, 9), random.randint(1, 9), random.randint(1, 9), random.randint(1, 9)
    for op1, op2, op3 in itertools.product(operators, repeat=3):
        if eval(f"{a}{op1}{b}{op2}{c}{op3}{d}") == e:
            return a, b, c, d, e
    return generate_equation()

def play_game():
    a, b, c, d = generate_equation()
    print(f"{a} _ {b} _ {c} = {d}")
    for attempt in range(3):
        user_input = input("Enter two operators separated by a space: ").split()
        if len(user_input) != 2:
            print("Invalid input. Please enter two operators separated by a space.")
            continue
        op1, op2 = user_input
        if eval(f"{a}{op1}{b}{op2}{c}") == d:
            print("Correct!")
            break
        else:
            print("Incorrect. Try again.")
    else:
        for op1, op2 in itertools.product(operators, repeat=2):
            if eval(f"{a}{op1}{b}{op2}{c}") == d:
                print(f"The correct answer is: {op1} {op2}")
                break

if __name__ == "__main__":
    play_game()
