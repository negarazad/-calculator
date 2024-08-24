#تابع توان

def power(num1, num2):
    return num1 ** num2
  
#-----------------------------------

#محاسبه رشه دوم
def square_root(num1):
    if num1 >= 0:
        return num1 ** 0.5
    else:
        return "Error! Negative number."

#------------------------------------

#محاسبه ی فاکتوریل
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

#-------------------------------------



