import random

results = []

start = input("Против кого играем? Компьютер или игрок? ").lower()

if start == "компьютер":
    continue_ = True
    game_count = 0

    while continue_:
        game_count += 1
        choice = input(f"Игра {game_count}. Выбор игрока (к/н/б): ").lower()
        
        if choice not in ["к", "н", "б"]:
            print("Неправильный ввод")
            continue

        comp_choice = random.choice(["к", "н", "б"])
        print(f"Выбор компьютера - {comp_choice}")

        combinations = [("б", "к"), ("к", "н"), ("н", "б")]
        if choice == comp_choice:
            result = "Ничья"
        elif (choice, comp_choice) in combinations:
            result = "Игрок выиграл"
        else:
            result = "Компьютер выиграл"

        results.append(result)

        print(result)

        continue_ = input("Желаете продолжить? Введите 'да' или 'нет': ").lower() == "да"

elif start == "игрок":
    game_count = 1

    player1_choice = input("Игрок 1, (к), (н), (б): ").lower()
    while player1_choice not in ['к', 'н', 'б']:
        print("Неверный выбор. Попробуйте еще раз.")
        player1_choice = input("Игрок 1, (к), (н), (б): ").lower()

    player2_choice = input("Игрок 2, (к), (н), (б): ").lower()
    while player2_choice not in ['к', 'н', 'б']:
        print("Неверный выбор. Попробуйте еще раз.")
        player2_choice = input("Игрок 2, (к), (н), (б): ").lower()

    if player1_choice == player2_choice:
        result = "Ничья!"
    elif (player1_choice == 'к' and player2_choice == 'н') or \
         (player1_choice == 'н' and player2_choice == 'б') or \
         (player1_choice == 'б' and player2_choice == 'к'):
        result = "Игрок 1 выиграл!"
    else:
        result = "Игрок 2 выиграл."

    results.append(result)

    print(result)

else:
    print("Неправильный выбор. Пожалуйста, введите 'компьютер' или 'игрок'.")

print("Результаты игр:")
for result in results:
    print(result)
