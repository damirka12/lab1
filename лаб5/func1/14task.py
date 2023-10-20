import math
import random
def guess_the_number(name):

    secret_number = random.randint(1, 100)
    attempts = 0
    print("Загадываю число...")
    while True:
        guess = input("Делай попытку.\n")
        try:
            guess = int(guess)
        except ValueError:
            print("Введи именно число. Мое число от 1 до 100.")
            continue

        attempts += 1

        if guess < secret_number:
            print("Твое число слишком маленькое.")
        elif guess > secret_number:
            print("Твое число слишком большое.")
        else:
            print(f"Ты угадал число за {attempts}\n{'Ты красавчик и логика у тебя на высшем уровне' if attempts <= 5 else 'Попробуй еще раз'}!")
            break




name = input("Привет! Как тебя зовут?\n")
print(f"Отлично, {name}, давай проверим твою интуициию! Сейчас я загадаю число от 1 до 100. Твоя задача отгадать это число за 5 попытok. Как по мне это более чем достаточно.")
print(f"Сейчас расскажу ход игры. "
          f"Ты вводишь любое число в диапазоне от 1 до 100"
          f"А я тебе даю подсказки, либо меньше, либо больше"
          f"Скажу по секрету, есть специальный алгоритм, как угадать число быстрее. Нооо, я его тебе не расскажу")
levaya = input("Ну что, поехали?\n")

beg = 0
while(beg == 0):
    guess_the_number(name)
    print("Понравилось? Хочешь еще? \n[1] - Да\n[2] - Нет")
    m = input()
    if(m == 'Нет' or m == 2):
        beg = 2
