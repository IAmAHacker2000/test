"""Данные из таблицы student.csv необходимо отсортировать по столбцу оценки(score) с помощь
сортировки вставками (В задаче нельзя использовать встроенные функции сортировок!). Из
полученного списка выделите первых 3х победителей из 10 класса. Данные о победителях
необходимо вывести в формате:
<X> класс:
1 место: <И. Фамилия>
2 место: <И. Фамилия>
3 место: <И. Фамилия>"""
import csv


def insertion_sort(array: list) -> list:
    """Функция сортировки вставками

    Описание аргументов:
    array: Массив который мы сорируем
    """
    n = len(array)
    for i in range(1, n):
        x = array[i]
        j = i

        while j > 0 and array[j - 1]["score"] < x["score"]:
            array[j] = array[j - 1]
            j -= 1
        array[j] = x
    return array


def convert_str(name):
    name1, name2, name3 = name.split()
    return f"{name2[0]}. {name1}"


def check_class(_class):
    data = list()
    with open("students.csv", encoding="utf-8") as file:
        reader = csv.DictReader(file, fieldnames=["id", "Name", "titleProject_id", "class", "score"])
        for r in reader:
            if _class in r["class"] and r["score"] != "None":
                data.append(r)

    sorted_list = insertion_sort(data)
    print(f"""{_class} класс:
1 место: {convert_str(sorted_list[0]["Name"])}
2 место: {convert_str(sorted_list[1]["Name"])}
3 место: {convert_str(sorted_list[2]["Name"])}""")


check_class("10")
