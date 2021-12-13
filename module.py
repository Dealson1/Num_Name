def Val(dic: dict)->list:
    """
    :param dict dic: Название словаря
    """
    mas = []
    for v in dic.values():
        mas.append(v.strip(''))
    return mas

def Key(dic: dict)->list:
    """
    :param dict dic: Название словаря
    """
    mas = []
    for v in dic.keys():
        mas.append(v.strip(''))
    return mas


def num_name(numb: list, lett: list, name: str):
    """
    :param list numb: Список с цифрами
    :param list lett: Список с буквами
    :param str name: Введенное имя
    """
    name_list = list(name)
    name_numbers = 0
    n = 0
    sum = 0
    for i in name_list:
        l = name_list[n]
        index = lett.index(l)
        numbers = numb[index]
        sum += int(numbers)
        n += 1

    sum1 = 0
    sum2 = 0
    sum3 = 0
    k = 0

    if sum < 10:
        text = f"Число имени - {sum}"
    elif sum >= 10:
        sum1 = sum % 10
        sum2 = sum // 10
        sum3 = sum1 + sum2
        if sum3 < 10:
            text = f"Число имени - {sum3}"
        elif sum3 >= 10:
            a = sum3 // 10
            b = sum3 % 10
            k = a + b
            text = f"Число имени - {k}"
    return text
