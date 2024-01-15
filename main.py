from function import *
from function import EditLists, FutureSalary, Kustutamine, Lisamine, RenameEveryThird

# Palgad
salary = [1200, 2500, 750, 395, 1200]
names = ['A', 'B', 'C', 'D', 'E']

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
    print("13 - Редактирование данных")
    print("14 - Рассчитать будущую зарплату через T лет")
    print("15 - Будущая зарплата")
    print("16 - Заменить имя")
    print("17 - Заменить зарплату")
    print("18 - Выйти")

    choice = int(input("Выберите действие: "))

    if choice == 1:
        k = int(input("Сколько людей добавить? "))
        names, salary = Lisamine(names, salary, k)
        for i in range(len(salary)):
            print(names[i], "сумма", salary[i])
    elif choice == 2:
        target_name = input("Введите имя для удаления: ")
        names, salary = Kustutamine(names, salary, target_name)
    elif choice == 3:
        sort_type = int(input("Выберите тип сортировки (1 - по убыванию, 2 - по возрастанию): "))
        names, salary = Sort(names, salary, sort_type)
        for i in range(len(salary)):
            print(names[i], "сумма", salary[i])
    elif choice == 4:
        maxpalk, nimi = Suurimpalk(names, salary)
        print(nimi, "сааб катта", maxpalk, "Eur")
    elif choice == 5:
        minpalk, nimi = Vahempalk(names, salary)
        print(nimi, "сааб катта", minpalk, "Eur")
    elif choice == 6:
        find_salary = int(input("Введите зарплату для поиска: "))
        people_with_salary = FindSameSalary(names, salary, find_salary)
        if people_with_salary:
            print(f"Люди с зарплатой {find_salary}:")
            for person in people_with_salary:
                print(person[0], "сумма", person[1])
            print(f"Всего {len(people_with_salary)} человек(а)")
    elif choice == 7:
        target_name = input("Введите имя для поиска зарплаты: ")
        found_salary = FindSalaryByName(names, salary, target_name)
        if found_salary is not None:
            print(f"{target_name} имеет зарплату {found_salary}")
        else:
            print(f"{target_name} не найдено в списке.")
    elif choice == 8:
        n_richest = int(input("Введите количество человек в топе: "))
        top_richest = Top(names, salary, n_richest)
        print(f"Топ {n_richest} самых богатых:")
        for person in top_richest:
            print(person[0], "сумма", person[1])
    elif choice == 9:
        n_poorest = int(input("Введите количество человек в топе: "))
        top_poorest = Top(names, salary, n_poorest, reverse=True)
        print(f"Топ {n_poorest} самых бедных:")
        for person in top_poorest:
            print(person[0], "сумма", person[1])
    elif choice == 10:
        avg_salary, person_with_avg_salary = Average(names, salary)
        print(f"Средняя зарплата: {avg_salary}")
        print(f"Человек с ближайшей зарплатой к средней: {person_with_avg_salary}")
    elif choice == 11:
        sort_reverse = input("Сортировать в обратном порядке? (y/n): ").lower() == 'y'
        names, salary = SortByName(names, salary, reverse=sort_reverse)
        for i in range(len(salary)):
            print(names[i], "сумма", salary[i])
    elif choice == 12:
        threshold = 700
        names, salary = RemoveBelowThreshold(names, salary, threshold)
        for i in range(len(salary)):
            print(names[i], "сумма", salary[i])
    elif choice == 13:
        names, salary = EditLists(names, salary)
        for i in range(len(salary)):
            print(names[i], "сумма", salary[i])
    elif choice == 14:
        target_name = input("Введите имя работника: ")
        target_index = names.index(target_name) if target_name in names else -1

        if target_index != -1:
            current_salary = salary[target_index]
            years = int(input("Введите количество лет: "))
            future_salary = FutureSalary(current_salary, years)
            print(f"Будущая зарплата для {target_name} через {years} лет: {future_salary}")
    elif choice == 15:
        names = RenameEveryThird(names)
        print("Список имен после переименования:")
        print(names)
    elif choice == 16:
        target_name = input("Введите имя для редактирования: ")
        new_name = input("Введите новое имя: ")
        if target_name in names:
            index = names.index(target_name)
            names[index] = new_name.capitalize()
            print(f"Имя {target_name} успешно изменено на {new_name}.")
        else:
            print(f"{target_name} не найдено в списке.")
    elif choice == 17:
        target_name = input("Введите имя для редактирования зарплаты: ")
        if target_name in names:
            index = names.index(target_name)
            new_salary = int(input("Введите новую зарплату: "))
            salary[index] = new_salary
            print(f"Зарплата для {target_name} успешно изменена на {new_salary}.")
        else:
            print(f"{target_name} не найдено в списке.")
    elif choice == 18:
        break
    else:
        print("Неверный выбор. Пожалуйста, выберите снова.")
