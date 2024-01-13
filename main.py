from Function import *

# Palgad
palgad = [1200, 2500, 750, 395, 1200]
inimesed = ['A', 'B', 'C', 'D', 'E']

while True:
    print("1 - Добавить данные")
    print("2 - Удалить по имени")
    print("3 - Сортировка по убыванию")
    print("4 - Максимальное значение")
    print("5 - Минимальное значение")
    print("6 - Найти зарплату")
    print("7 - Найти зарплату по имени")
    print("8 - Найти самых богатых")
    print("9 - Найти самих бедных")
    print("10 - Средняя зарплата")
    print("11 - Сортировка по имени")
    print("12 - Удаление тех, у кого зарплата меньше минимальной")

    choice = int(input("Выберите действие: "))

    if choice == 1:
        k = int(input("Сколько людей добавить? "))
        inimesed, palgad = Lisamine(inimesed, palgad, k)
        for i in range(len(palgad)):
            print(inimesed[i], "сумма", palgad[i])
    elif choice == 2:
        target_name = input("Введите имя для удаления: ")
        inimesed, palgad = Kustutamine(inimesed, palgad, target_name)
    elif choice == 3:
        sort_type = int(input("Выберите тип сортировки (1 - по убыванию, 2 - по возрастанию): "))
        inimesed, palgad = Sort(inimesed, palgad, sort_type)
        for i in range(len(palgad)):
            print(inimesed[i], "сумма", palgad[i])
    elif choice == 4:
        maxpalk, nimi == Suurimpalk(inimesed, palgad)
        print(nimi,"saab kätta", maxpalk, "Eur")
    elif choice == 5:
        minpalk, nimi == Vahempalk(inimesed, palgad)
        print(nimi,"saab kätta", maxpalk, "Eur")
    elif choice == 6:
        find_salary = int(input("Введите зарплату для поиска: "))
        people_with_salary = FindSameSalary(inimesed, palgad, find_salary)
        if people_with_salary:
            print(f"Люди с зарплатой {find_salary}:")
            for person in people_with_salary:
                print(person[0], "сумма", person[1])
            print(f"Всего {len(people_with_salary)} человек(а)")
    elif choice == 7:
        target_name = input("Введите имя для поиска зарплаты: ")
        salary = FindSalaryByName(inimesed, palgad, target_name)
        if salary is not None:
            print(f"{target_name} имеет зарплату {salary}")
    elif choice == 8:
        n_richest = int(input("Введите количество человек в топе: "))
        top_richest = Top(inimesed, palgad, n_richest)
        print(f"Топ {n_richest} самых богатых:")
        for person in top_richest:
            print(person[0], "сумма", person[1])
    elif choice == 9:
        n_poorest = int(input("Введите количество человек в топе: "))
        top_poorest = Top(inimesed, palgad, n_poorest, reverse=True)
        print(f"Топ {n_poorest} самых бедных:")
        for person in top_poorest:
            print(person[0], "сумма", person[1])
    elif choice == 10:
        avg_salary, person_with_avg_salary = Average(inimesed, palgad)
        print(f"Средняя зарплата: {avg_salary}")
        print(f"Человек с ближайшей зарплатой к средней: {person_with_avg_salary}")
    elif choice == 11:
        sort_reverse = input("Сортировать в обратном порядке? (y/n): ").lower() == 'y'
        inimesed, palgad = SortByName(inimesed, palgad, reverse=sort_reverse)
        for i in range(len(palgad)):
            print(inimesed[i], "сумма", palgad[i])
    elif choice == 10:
        threshold = 700
        inimesed, palgad = RemoveBelowThreshold(inimesed, palgad, threshold)
        for i in range(len(palgad)):
            print(inimesed[i], "сумма", palgad[i])
    else:
        print("Неверный выбор. Пожалуйста, выберите снова.")
    

