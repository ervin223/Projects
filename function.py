﻿
def Lisamine(names: list, salaries: list, amount: int):
    """
    Функция для добавления имен и зарплат в списки names и salaries.

    :param names: Список имен.
    :param salaries: Список зарплат.
    :param amount: Количество людей, которых необходимо добавить.
    :rtype:list.
    """
    for _ in range(amount):
        name = input("Mis on nimi? ")
        salary = int(input("Mis suur palk on: "))
        names.append(name)
        salaries.append(salary)

    return names, salaries


def Kustutamine(names: list, salaries: list, target_name: str):
    """
        Удаляет людей из списка.

    :param names: Список имен.
    :param salaries: Список зарплат.
    :param target_name: Имя для поиска.
    :rtype: Удаленный список.
    """
    if target_name in names:
        index = names.index(target_name)
        names.pop(index)
        salaries.pop(index)
        print(f"{target_name} успешно удален.")
    else:
        print(f"{target_name} не найден в списке.")

    return names, salaries


def Suurimpalk(names: list, salaries: list):
    """
        Ищет людей с наивысшей зарплатой.

    :param names: Список имен.
    :param salaries: Список зарплат.
    :param target_salary: Зарплата для поиска.
    :rtype: Список людей с наивысшей зарплатой.
    """
    max_ = max(salaries)
    ind = salaries.index(max_)
    nimi = names[ind]
    for palk in salaries:
        if palk == max_:
            ind = salaries.index
    
    return max_, nimi


def Sort(names: list, salaries: list, a: int):
    """
    Сортирует людей по убыванию или возрастанию
    
        Ищет людей с заданной зарплатой.

    :param names: Список имен.
    :param salaries: Список зарплат.
    :rtype: Сортиованыый список.
    """
    n = len(names)
    if a == 1:
        for i in range(0, n + 1):
            for m in range(n, n + 1):
                if salaries[n] < salaries[m]:
                    kaust = salaries[n]
                    salaries[n] = salaries[m]
                    salaries[m] = kaust
                    kaust = names[n]
                    names[n] = names[m]
                    names[m] = kaust
    else:
        pass
    return names, salaries

def Vahempalk(names: list, salaries: list):
    """
     Находит минимальную зарплату

    :param names: Список имен.
    :param salaries: Список зарплат.
    :rtype: Список людей с минимальной зарплатой.
    """
    min_ = min(salaries)
    ind = salaries.index(min_)
    nimi = names[ind]
    for palk in salaries:
        if palk == min_:
            ind = salaries.index
    
    return min_, nimi


def FindSameSalary(names: list, salaries: list, target_salary: int):
    """
    Ищет людей с заданной зарплатой.

    :param names: Список имен.
    :param salaries: Список зарплат.
    :param target_salary: Зарплата для поиска.
    :rtype: Список людей с заданной зарплатой.
    """
    people_with_salary = [(name, salary) for name, salary in zip(names, salaries) if salary == target_salary]
    return people_with_salary

def FindSalaryByName(names: list, salaries: list, target_name: str):
    """
    Ищет зарплату по имени человека.

    :param names: Список имен.
    :param salaries: Список зарплат.
    :param target_name: Имя для поиска.
    :rtype: Зарплата человека с указанным именем.
    """
    if target_name in names:
        index = names.index(target_name)
        return salaries[index]
    else:
        print(f"{target_name} не найден в списке.")
        return None

def Top(names: list, salaries: list, n: int, reverse: bool = False):
    """
    Возвращает топ N самых богатых или бедных людей.

    :param names: Список имен.
    :param salaries: Список зарплат.
    :param n: Количество человек в топе.
    :param reverse: Если True, возвращает топ самых бедных, иначе - самых богатых.
    :rtype: Список кортежей с именами и зарплатами топ N людей.
    """
    combined_data = list(zip(names, salaries))
    sorted_data = sorted(combined_data, key=lambda x: x[1], reverse=reverse)
    return sorted_data[:n]


def Average(names: list, salaries: list):
    """
    Находит среднюю зарплату и имя человека, получающего эту зарплату.

    :param names: Список имен.
    :param salaries: Список зарплат.
    :rtype: Кортеж из средней зарплаты и имени человека, получающего эту зарплату.
    """
    average_salary = sum(salaries) / len(salaries)
    closest_salary = min(salaries, key=lambda x: abs(x - average_salary))
    closest_person_index = salaries.index(closest_salary)
    closest_person_name = names[closest_person_index]
    return average_salary, closest_person_name

def SortByName(names: list, salaries: list, reverse: bool = False):
    """
    Сортирует списки по имени.

    :param names: Список имен.
    :param salaries: Список зарплат.
    :param reverse: Если True, сортирует в обратном порядке.
    :rtype: Отсортированные списки по имени.
    """
    combined_data = list(zip(names, salaries))
    sorted_data = sorted(combined_data, key=lambda x: x[0], reverse=reverse)
    return list(zip(*sorted_data))


def RemoveBelowThreshold(names: list, salaries: list, threshold: int):
    """
    Находит и удаляет тех, кто получает зарплату ниже заданного порога.

    :param names: Список имен.
    :param salaries: Список зарплат.
    :param threshold: Пороговая зарплата для удаления.
    :rtype: Отфильтрованные списки без людей с зарплатой ниже порога.
    """
    filtered_data = [(name, salary) for name, salary in zip(names, salaries) if salary >= threshold]
    return list(zip(*filtered_data))


def EditLists(names: list, salaries: list):
    """
    Редактирует списки, приводя имена к формату с большой буквы и зарплаты к формату int.

    :param names: Список имен.
    :param salaries: Список зарплат.
    :rtype: Отредактированные списки.
    """
    edited_names = [name.capitalize() for name in names]
    edited_salaries = [int(salary) for salary in salaries]
    return edited_names, edited_salaries

def FutureSalary(salary: int, years: int):
    """
    Рассчитывает будущую зарплату работника через T лет с учетом ежегодного повышения на 5%.

    :param salary: Текущая зарплата.
    :param years: Количество лет.
    :rtype: Будущая зарплата.
    """
    annual_increase = 0.05  
    future_salary = salary * (1 + annual_increase) ** years
    return future_salary

def FutureSalary(salary: int, years: int):
    """
    Рассчитывает будущую зарплату работника через T лет с учетом ежегодного повышения на 5%.

    :param salary: Текущая зарплата.
    :param years: Количество лет.
    :rtype: Будущая зарплата.
    """
    annual_increase = 0.05  
    future_salary = salary * (1 + annual_increase) ** years
    return future_salary

def RenameEveryThird(names: list):
    """
    Переименовывает каждого третьего человека. Новые имена вводит пользователь.

    :param names: Список имен.
    :rtype: Обновленный список имен.
    """
    for i in range(2, len(names), 3):
        new_name = input(f"Введите новое имя для {names[i]}: ")
        names[i] = new_name.capitalize()
    return names

def EditData(names: list, salaries: list):
    """
    Редактирует данные в списках. Пользователь выбирает, что редактировать: имя или зарплату.

    :param names: Список имен.
    :param salaries: Список зарплат.
    :rtype: Обновленные списки.
    """
    print("1 - Редактировать имя")
    print("2 - Редактировать зарплату")

    choice = int(input("Выберите, что редактировать: "))
    
def Vocfind(names: list, salaries: list, letter: str):
    """
    Функция для поиска имен, начинающихся на заданную букву, и отображения их зарплат.

    :param names: Список имен.
    :param salaries: Список зарплат.
    :param letter: Буква для поиска.
    :rtype: таблица
    """
    found_names = [name for name in names if name.lower().startswith(letter.lower())]
    
    if found_names:
        for name in found_names:
            index = names.index(name)
            print(f"{name} - {salaries[index]}")
    else:
        print(f"Нет имен, начинающихся с буквы {letter}.")
    






