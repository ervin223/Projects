import random

total_questions = int(input("How many quastions you want to solve? "))
difficulty = int(input("Write lvl (1, 2, 3): "))

correct_answers = 0

for i in range(total_questions):
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10) if difficulty == 1 else random.randint(10, 100) if difficulty == 2 else random.randint(100, 1000)

    operator = random.choice(['+', '-', '*'])
    question = f"{num1} {operator} {num2}"
    correct_answer = eval(question)

    user_answer = float(input(f"Solve quastion: {question} = "))

    if user_answer == correct_answer:
        print("Correct!")
        correct_answers += 1
    else:
        print(f"Wrong. Correct answer is: {correct_answer}")

percentage_correct = (correct_answers / total_questions) * 100
print(f"\nHinne: {percentage_correct}%")

if percentage_correct < 60:
    print("Hinne 2")
elif 60 <= percentage_correct < 75:
    print("Hinne 3")
elif 75 <= percentage_correct < 90:
    print("Hinne 4")
else:
    print("Hinne 5")
