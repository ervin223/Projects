
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
    :return: Зарплата человека с указанным именем.
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
    :return: Список кортежей с именами и зарплатами топ N людей.
    """
    combined_data = list(zip(names, salaries))
    sorted_data = sorted(combined_data, key=lambda x: x[1], reverse=reverse)
    return sorted_data[:n]


def Average(names: list, salaries: list):
    """
    Находит среднюю зарплату и имя человека, получающего эту зарплату.

    :param names: Список имен.
    :param salaries: Список зарплат.
    :return: Кортеж из средней зарплаты и имени человека, получающего эту зарплату.
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
    :return: Отсортированные списки по имени.
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
    :return: Отфильтрованные списки без людей с зарплатой ниже порога.
    """
    filtered_data = [(name, salary) for name, salary in zip(names, salaries) if salary >= threshold]
    return list(zip(*filtered_data))



