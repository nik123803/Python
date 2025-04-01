# Перевірка парності
# Створіть функцію, яка приймає число та повертає True,
#  якщо воно парне, і False, якщо непарне.
# def Parity_check(number):
#     if isinstance(number, bool) or not isinstance(number, (float, int)):
#         return "Некоректні дані" 
#     elif number % 2 == 0:
#         return "Число " + str(number) + " є парним!"    
#     else:
#         return "Число " + str(number) + " є не парне"

# number = 10
# print(Parity_check(number))
# number = 11
# print(Parity_check(number))
# number = 120
# print(Parity_check(number))
# number = "ABC"
# print(Parity_check(number))
# number = False
# print(Parity_check(number))

# Вивід трикутника
# Функція приймає число n і друкує трикутник висотою n з *.

# def triangle(n):
#     for i in range(1, n + 1):
#         print(" " * i)

# triangle(5)

# Оцінка за балами
# Напишіть функцію, яка приймає оцінку (0-100) і повертає рівень (A, B, C, D, F).

# A: 90 - 100
# ﻿﻿B: 80 - 89
# . C: 70 - 79
# ﻿﻿D: 60 - 69
# ﻿﻿F: 0 - 59
 
# 2

# Перевірка високосного року
# Створіть функцію, яка приймає рік та повертає True, якщо
#  це високосний рік, і False, якщо ні.
# У григоріанському календарі, високосні роки визначаються таким чином: кожен рік, який ділиться на чотири, є високосним, за винятком років, які діляться на 100, але не діляться на 400. Наприклад, 1700, 1800 і 1900 роки невисокосні, а 1600 і 2000 — високосні.
# def leaping(year):
#     if year % 4 == 0 and year % 100 != 0:
#         return "Рік високосний"
#     elif year % 400 == 0:     
#         return "Рік високосний"
#     else:
#         return "Рік не високосний"   

# year = int(input("Перевірка високосного року:"))   
# print(leaping(year))    

# Перетворення градусів
# Реалізуйте функцію, яка перетворює температуру з Цельсія у Фаренгейти та навпаки (на основі другого аргументу C або F).

# def Temperature(C, F):
#     if isinstance(F, bool):
#         return "Некоректні дані"
#     elif F == "f" or F == "F":   
#         return C * 9 / 5 + 32  
#     elif F == "c" or F == "C":   
#         return (C - 32) * 5 / 9  

# accept = int(input("Введіть градуси:"))
# accept2 = input("C або F:")
# print(Temperature(accept, accept2))

# def primer(n):
#     for nun in range (2, n + 1):
#         if (nun % 2 != 0 and nun % 3 != 0 and nun % 5 != 0):
#             print(nun)
     
# primer(1000)


# Форма звернення
# Функція приймає стать (M або F) та вік і повертає відповідну форму звернення: "Пане" або "Пані", з урахуванням віку.

# def Application_form(Sex, Age):
#     if Sex == "M" or Sex == "m":
#         if Age < 25:
#             return "Доброго дня, Юначе!"
#         elif Age < 60:
#             return "Доброго дня, Пане!"  
#         elif Age < 100:
#             return "Доброго дня, Дідусю!" 
#         else:
#             return "Некоректні дані!"         
#     elif Sex == "F" or Sex == "f":
#         if Age < 25:
#             return "Доброго дня, Дівчино!"
#         elif Age < 60:
#             return "Доброго дня, Пані!"  
#         elif Age < 100:
#             return "Доброго дня, Бабусю!" 
#         else:
#             return "Некоректні дані!"         
#     else:
#         return "Некоректні дані!"        

# sex = input("Введіть свою стать:")        
# age = int(input("Введіть свій вік:"))  
# print(Application_form(sex, age)) 


# Тарифи на оплату
# Функція приймає кількість кіловат-годин і повертає вартість електроенергії за умовами тарифного плану (залежно від кількості спожитої енергії).

# def Kilowatt_hour(was, became, tariff):
#     if became == 0 or tariff == 0:
#         return "Некоректні дані!"
#     else: 
#         return((became - was) * tariff) 
        
# was = int(input("Введіть попереднє значення:")) 
# became = int(input("Введіть нинішне значення:"))   
# tariff = float(input("Введіть ваш тарифний план:"))
# print(Kilowatt_hour(was, became, tariff))

# Сума цифр числа
# Функція приймає число і повертає суму його цифр.

# def sum_numbers(numbers):
#     sum = 0
#     for i in numbers:
#         i = int(i)
#         sum += i
#     return sum    
# print(sum_numbers("2498"))

# Реверс числа
# Функція приймає число і повертає його дзеркальне значення (наприклад, 123 -> 321).
# def Numbers_versa(numbers):
#     return int(str(numbers)[::-1])
# print(Numbers_versa(1234))   


# Піднесення до степеня
# Функція приймає два числа a та n і повертає a
# в степені n, не використовуючи ** або pow().

# def Stepin(numbers1, numbers2):
#     result = 1
#     for _ in range(numbers2):
#         result *= numbers1
#     return result    

# print(Stepin(10, 5))

# Перетворення часу
# Функція приймає кількість секунд та
# повертає формат години:хвилини:секунди. За замовчуванням секунди=3600.


# 1. Час у годинах: Поділити кількість секунд на 3600 (це кількість секунд в одній годині).
# 2. Час у хвилинах: Залишок від поділу на 3600 (це залишок секунд після віднімання годин) поділити на 60 (це кількість секунд в одній хвилині).
# 3. Залишок секунд: Залишок після поділу на 60 дає кількість залишкових секунд.

# Наприклад, для 5000 секунд:

# 1. 5000 / 3600 = 1 година (залишок: 5000 - 3600 = 1400 секунд)
# 2. 1400 / 60 = 23 хвилини (залишок: 1400 - 23*60 = 20 секунд)

# Отже, 5000 секунд = 1 година, 23 хвилини, 20 секунд.


# def Time_conversion(time):
#     hour = time // 3600
#     minutes = (time % 3600) // 60
#     seconds = time % 60
#     print(f"Годин: {hour}, Хвилин: {minutes}, Секунди: {seconds}.")

# Time_conversion(5000)

# Оцінка успішності
# Функція приймає 8 балів студента, вираховує середнє значення
# та перевіряє чи бали не менше 60, якщо вони нижче 60 то студент
# провалив сесію, інакше сесія успішно закрита і на основі середнього значення
# повертаємо чи студент трійник, ударник чи відмінник.

# 40

# Задача 1. Конвертер валют
# Написати функцію convert_currency(amount, rate), яка перетворює суму amount з однієї валюти в іншу за
# курсом rate. print(convert_currency(100, 39.5))  # 3950.0 (наприклад, USD → UAH)

# def convert_currency(amount, rate):
#     Currency = float(amount * rate)
#     return print(Currency)  
# convert_currency(1001, 41.25)

# Задача 2. Валідатор паролю
# Написати функцію check_password(password), яка перевіряє, чи містить пароль
# щонайменше 8 символів, одну цифру та одну велику літеру.
# fo

# Задача 3. Форматування номера телефону
# Написати функцію format_phone(number), яка перетворює введений номер телефону 
# в стандартний формат +38 (XXX) XXX-XX-XX.
# import re
# def format_phone(number):
#     digits = re.sub(r'\D', '', number)
#     if len(digits) == 10:
#         digits = '38' + digits
#     elif len(digits) != 12:
#         return "Невірний формат номера"
    
#     parts = [digits[:2], digits[2:5], digits[5:8], digits[8:10], digits[10:12]]
#     formatted = "+{} ({}) {}-{}-{}".format(*parts)
#     print(formatted)
     
     
# format_phone("0993467893")   
# format_phone("380973467893")   
# format_phone("+380992066893")   


# Задача 4. Генератор паролів
# Написати функцію generate_password(length), яка створює випадковий пароль заданої довжини.
# print(generate_password(12))  # Наприклад: G#2f@9dL!kM8

# def analyze_expenses(transactions):
#     expenses = {}
#     for category, amount in transactions:
#         if category in expenses:
#             expenses[category] += amount
#         else:
#             expenses[category] = amount
#     return expenses 

# transactions = [
#     ("Їжа", 200), 
#     ("Транспорт", 150), 
#     ("Їжа", 300), 
#     ("Розваги", 500)
# ]

# result = analyze_expenses(transactions)
# print(result)  
                                                                                                                                                    
# from collections import Counter
# Name_students = ['Микита', 'Владислав', 'Андрій', 'Віка', 'Анастасія', 'Владислав']
# def Find_letters(Name):
#     letters = list("".join(Name).lower())
#     count_letters = Counter(letters)
#     print(count_letters)

# Find_letters(Name_students)

# def number_to_words(n):
#     if not (1 <= n <= 999):  
#         return "Число має бути в межах 1-999"

#     ones = ["", "один", "два", "три", "чотири", "п'ять", "шість", "сім", "вісім", "дев'ять"]
#     teens = ["десять", "одинадцять", "дванадцять", "тринадцять", "чотирнадцять", 
#              "п'ятнадцять", "шістнадцять", "сімнадцять", "вісімнадцять", "дев'ятнадцять"]
#     tens = ["", "десять", "двадцять", "тридцять", "сорок", "п'ятдесят", 
#             "шістдесят", "сімдесят", "вісімдесят", "дев'яносто"]
#     hundreds = ["", "сто", "двісті", "триста", "чотириста", "п'ятсот", 
#                 "шістсот", "сімсот", "вісімсот", "дев'ятсот"]

#     result = []  
  
#     h = n // 100       
#     t = (n % 100) // 10  
#     o = n % 10        

#     if h > 0:
#         result.append(hundreds[h])  

   
#     if t == 1: 
#         result.append(teens[o])  
#         if t > 1:
#             result.append(tens[t])  
#         if o > 0:
#             result.append(ones[o])  

#     return " ".join(result) 

# print(number_to_words(123))  


def analyze_expenses():
    user_input = input("Введіть суми витрат на продукти за тиждень через кому: ")
    expenses = [float(x.strip()) for x in user_input.split(",")]
    total_expense = sum(expenses)
    print(f"Загальні витрати за тиждень: {total_expense:.2f} грн")
    if total_expense > 1000:
        print("Увага! Ви перевищили бюджет на продукти. Спробуйте економити!")
    else:
        print("Чудово! Ви вкладаєтесь у бюджет на продукти.")


analyze_expenses()

# Планувальник завдань
# Напишіть програму, яка запитує у користувача список завдань (наприклад, "купити молоко, прибрати, попрацювати")
# і кількість годин у змінній hours. Використовуйте цикл для підрахунку кількості завдань і умовну конструкцію, 
# щоб визначити, чи вистачить часу (вважайте, що одне завдання = 1 година). Виведіть результат.

# Запитуємо у користувача список завдань


def Tasks_for_the_day():
 tasks = input("Введіть список завдань через кому: ".split(","))
 tasks = [task.strip() for task in  tasks]
 num_tasks = len(tasks)
 hours = int(input("Скільки у вас годин? "))
 if hours >= num_tasks:
    print(f"Чудово! Ви встигнете виконати всі {num_tasks} завдань.")
 else:
    print(f"У вас лише {hours} годин, а завдань {num_tasks}. Доведеться вибрати найважливіші.")