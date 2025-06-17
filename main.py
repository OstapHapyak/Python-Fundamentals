import random

user_input = int(input("Введіть число від 0 до 100: "))
random_number = random.randint(0, 100)

print("Виграшне число:", random_number)

if user_input == random_number:
    print("Вітаю! Ви виграли!")
