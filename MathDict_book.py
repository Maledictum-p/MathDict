import json
from json.decoder import JSONDecodeError
import random


class Book:
    def __init__(self):
        self.classes = ["./class_1.txt", "./class_2.txt", "./class_3.txt", "./class_4.txt"]
        self.exercises = dict()
        self.class_work = ""
        self.menu_start()

    def add_exercise(self):
        new_problems = []
        new_answers = []
        new_exercise = []
        number = int(input("Введите номер задачи:"))
        for i in range(10):
            print("Введите условие %s: " % str(i + 1), end="")
            new_problems.append(input())
            print("Введите ответ %s: " % str(i + 1), end="")
            new_answers.append(int(input()))
        new_exercise.append([new_problems, new_answers])
        self.exercises.update({number: new_exercise})
        print("OK")

    def menu_start(self):
        answer = ""
        while answer != "exit":
            print("Введите команду:")
            print("Решать задачи: solve")
            print("Вносить задачи: update")
            print("Выход: exit")
            answer = input()
            if answer == "solve":
                pass
                self.get_class()
                self.solve()
            elif answer == "update":
                pass
                self.get_class()
                self.update()
        print("До скорых встреч")

    def get_class(self):
        answer = ""
        answers = ["1", "2", "3", "4"]
        while answer != "exit":
            print("Введите класс:")
            print("1 класс: 1")
            print("2 класс: 2")
            print("3 класс: 3")
            print("4 класс: 4")
            answer = input()
            if answer in answers:
                self.class_work = self.classes[int(answer) - 1]
                self.download_file()
                answer = "exit"

    def exist_files(self):
        for i in self.classes:
            try:
                file = open(i)
                file.close()
            except FileNotFoundError:
                file = open(i, "w")
                file.close()

    def download_file(self):
        self.exist_files()
        try:
            with open(self.class_work) as file:
                self.exercises = json.load(file)
        except JSONDecodeError:
            pass

    def upload_file(self):
        self.exist_files()
        with open(self.class_work, "w") as file:
            json.dump(self.exercises, file, indent=4)

    def update(self):
        answer = ""
        while answer != "exit":
            print("Ввести задачу?:")
            print("Да: 1")
            print("Нет : exit")
            answer = input()
            if answer == "1":
                self.add_exercise()
        self.upload_file()

    def solve(self):
        answer = ""
        while answer != "exit":
            print("Решать задачу?:")
            print("Да: 1")
            print("Нет : exit")
            answer = input()
            if answer == "1":
                random.seed()
                ex_num = random.randint(1, len(self.exercises))
                answers = []
                exercise = self.exercises[str(ex_num)]
                print("Ответьте на вопросы:")
                for i in range(10):
                    print(exercise[0][0][i])
                    answers.append(int(input("Ответ:")))
                print("Результаты:")
                for i in range(10):
                    if exercise[0][1][i] == answers[i]:
                        print("Вопрос %s: решен верно, ответ: %s" % (i + 1, answers[i]))
                    else:
                        print("Вопрос %s: решен неверно, ваш ответ: %s, правильный ответ: %s" % (
                        i + 1, answers[i], exercise[0][1][i]))


if __name__ == "__main__":
    new_game = Book()
