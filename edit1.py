# تعریف توابع برای عملیات‌های ریاضی
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Error! Division by zero."

# تابع اصلی ماشین حساب
def calculator():
    operations = {
        '1': add,
        '2': subtract,
        '3': multiply,
        '4': divide
    }

    while True:
        # دریافت عدد اول از کاربر
        first_input = input("Enter the first number (or type 'end' to exit): ")
        if first_input.lower() == 'end':
            print("Exiting the calculator. Goodbye!")
            break
        try:
            num1 = float(first_input)
        except ValueError:
            print("Invalid input! Please enter a numeric value or 'end' to exit.")
            continue

        # دریافت عدد دوم از کاربر
        second_input = input("Enter the second number (or type 'end' to exit): ")
        if second_input.lower() == 'end':
            print("Exiting the calculator. Goodbye!")
            break
        try:
            num2 = float(second_input)
        except ValueError:
            print("Invalid input! Please enter a numeric value or 'end' to exit.")
            continue

        # نمایش منوی عملیات‌ها
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")

        # دریافت انتخاب کاربر
        choice = input("Enter choice (1/2/3/4) or 'end' to exit: ")

        if choice.lower() == 'end':
            print("Exiting the calculator. Goodbye!")
            break

        # انجام عملیات بر اساس انتخاب کاربر
        if choice in operations:
            result = operationschoice
            print(f"The result is: {result}")
        else:
            print("Invalid choice! Please select a valid operation.")

# اجرای تابع ماشین حساب
calculator()
