Аналізатор витрат на продукти
Напишіть програму, яка запитує у користувача суми витрат на продукти за тиждень (вводяться через кому, наприклад, 
"120, 350, 80"). Використовуйте змінні для зберігання загальної суми, цикл для обробки введених даних, умовну конструкцію 
для визначення, чи перевищують витрати 1000 грн, і виведіть повідомлення про економію або перевитрату.

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
