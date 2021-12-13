from module import *
from tkinter import *
dict = {"А": "1", "Б": "2", "В": "3", "Г": "4", "Д": "5", "Е": "6", "Ё": "7", "Ж": "8", "З": "9", "И": "1", "Й": "2", "К": "3", "Л": "4", "М": "5", "Н": "6", "О": "7", "П": "8", "Р": "9", "С": "1", "Т": "2", "У": "3", "Ф": "4", "Х": "5", "Ц": "6", "Ч": "7", "Ш": "8", "Щ": "9", "Ъ": "1", "Ы": "2", "Ь": "3", "Э": "4", "Ю": "5", "Я": "6"}
letters_list = readDictKeys(dict)
numb_list = readDictVal(dict)
def readDictVal(dic: dict)->list:
    """
    Читает значения из словаря и добавляем их в список
    :param dict dic: Название словаря
    """
    mas = []
    for v in dic.values():
        mas.append(v.strip(''))
    return mas

def readDictKeys(dic: dict)->list:
    """
    Читаем ключи из словаря и добавляем их в список
    :param dict dic: Название словаря
    """
    mas = []
    for v in dic.keys():
        mas.append(v.strip(''))
    return mas

def getNameNumber(numb: list, lett: list, name: str):
    """
    Берем введеное имя и раскладываем его в список. Сравниваем буквы из имени с буквами и их значениями из готового списка. Считаем полученные цифры и раскладываем сумму, если нужно
    :param list numb: Список с цифрами
    :param list lett: Список с буквами
    :param str name: Введенное имя
    """
    name_list = list(name)
    print(name_list)
    name_numbers = 0
    n = 0
    sum = 0
    for i in name_list:
        l = name_list[n]
        index = lett.index(l)
        numbers = numb[index]
        sum += int(numbers)
        n += 1

    print(sum)
    sum1 = 0
    sum2 = 0
    sum3 = 0
    k = 0

    if sum < 10:
        text = (f"Число имени - {sum}")
    elif sum >= 10:
        sum1 = sum % 10
        sum2 = sum // 10
        sum3 = sum1 + sum2
        if sum3 < 10:
            text = (f"Число вашего имени - {sum3}")
        elif sum3 >= 10:
            a = sum3 // 10
            b = sum3 % 10
            k = a + b
            text = (f"Число вашего имени - {k}")
    return text


def out(event):
    while True:
        try:
            name = ent1.get()
            verif = name.isalpha()

        except ValueError:
            print("Введите имя, состоящее из букв.")

        if verif == True:
            nameu = name.upper()
            text = getNameNumber(numb_list, letters_list, nameu)
            lbl3.configure(text = text)

window = Tk()
window.title("Num - Name")
window.geometry("600x300")

lbl1 = Label(window, text = "Нумерология - Число имени", font = "Arial 15")
lbl2 = Label(window, text = "Введите имя, состоящее из букв: ", font = "Arial 15")
ent1 = Entry(bg = "lightblue", width = 10, font = "Arial 15")
btn = Button(window, text = "Посчитать", font = "Arial 15", fg = "Black", bg = "lightgreen", width = 8, height = 1)
lbl3 = Label(text = "", font = "Arial 15", bg = "lightyellow")

btn.bind("<Button-1>", out)
ent1.bind("<Return>")

lbl1.pack()
lbl2.pack()
ent1.pack()
btn.pack()
lbl3.pack()

window.mainloop()