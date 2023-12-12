"""Все ребята сдали свои проекты и получили оценки на защите, но Виноградова Дарья все прослушал
и просит помочь ему узнать какую оценку за проект он получил. Пожалуйста, подскажите
Владимиру какую оценку он получил. Формат вывода: Ты получил: <ОЦЕНКА>, за проект - <id>
Пока помогали Владимиру увидели, что многие ученики потеряли свои оценки при выкачке с
сайта. Из-за этого нет возможности посмотреть общую статистику. Чтобы избежать путаницы
поставьте вместо ошибки среднее значение по классу и округлите до трех знаков после запятой.
Сохраните данные в новую таблицу с названием student_new.csv."""
import csv

summ = dict()
amount = dict()
with open("students.csv", encoding="utf-8") as file:
    reader = csv.DictReader(file, fieldnames=["id", "Name", "titleProject_id", "class", "score"])
    for r in reader:
        if r["score"] == "score":
            continue
        if r["score"] != "None":
            if r["class"] not in summ:
                summ[r["class"]] = 0
                amount[r["class"]] = 0
            summ[r["class"]] += int(r["score"])
            amount[r["class"]] += 1

        if "Виноградова Дарья" in r["Name"]:
            print(f"Ты получил: {r['score']}, за проект - {r['titleProject_id']}")

with open("students.csv", encoding="utf-8") as file, open("student_new.csv", "w", encoding="utf-8",
                                                          newline="") as _file:
    writer = csv.DictWriter(_file, fieldnames=["id", "Name", "titleProject_id", "class", "score"])
    writer.writeheader()
    reader = csv.DictReader(file, fieldnames=["id", "Name", "titleProject_id", "class", "score"])

    for r in reader:
        if r["score"] == "score":
            continue
        print(r)
        if r["score"] != "None":
            writer.writerow(r)
        else:
            new_r = r
            new_r["score"] = round(summ[r["class"]] / amount[r["class"]], 3)
            writer.writerow(new_r)
