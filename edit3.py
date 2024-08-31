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

def power(num1, num2):
    return num1 ** num2

def square_root(num1):
    if num1 >= 0:
        return num1 ** 0.5
    else:
        return "Error! Negative number."

def factorial(num1):
    if num1 < 0:
        return "Error! Negative number."
    elif num1 == 0:
        return 1
    else:
        result = 1
        for i in range(1, num1 + 1):
            result *= i
        return result

# تابع اصلی ماشین حساب
def calculator():
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

        # نمایش منوی عملیات‌ها
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Power")
        print("6. Square Root")
        print("7. Factorial")

        # دریافت انتخاب کاربر
        choice = input("Enter choice (1/2/3/4/5/6/7) or 'end' to exit: ")

        if choice.lower() == 'end':
            print("Exiting the calculator. Goodbye!")
            break

        # دریافت عدد دوم از کاربر (برای عملیات‌هایی که نیاز به دو عدد دارند)
        if choice in ['1', '2', '3', '4', '5']:
            second_input = input("Enter the second number (or type 'end' to exit): ")
            if second_input.lower() == 'end':
                print("Exiting the calculator. Goodbye!")
                break
            try:
                num2 = float(second_input)
            except ValueError:
                print("Invalid input! Please enter a numeric value or 'end' to exit.")
                continue

        # انجام عملیات بر اساس انتخاب کاربر
        if choice == '1':
            print(f"The result is: {add(num1, num2)}")
        elif choice == '2':
            print(f"The result is: {subtract(num1, num2)}")
        elif choice == '3':
            print(f"The result is: {multiply(num1, num2)}")
        elif choice == '4':
            print(f"The result is: {divide(num1, num2)}")
        elif choice == '5':
            print(f"The result is: {power(num1, num2)}")
        elif choice == '6':
            print(f"The result is: {square_root(num1)}")
        elif choice == '7':
            print(f"The result is: {factorial(int(num1))}")
        else:
            print("Invalid choice! Please select a valid operation.")

# اجرای تابع ماشین حساب
calculator()
