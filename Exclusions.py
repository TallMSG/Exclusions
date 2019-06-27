a, b, c = input('Enter values: ').split()
x = [a, b, c]
y = []
for item in x:
    a = x[0]
    b = int(x[1])
    c = int(x[2])
    y = [a, b, c]

def calculate(list_var):
    if list_var[0] == "*":
        return list_var[1] * list_var[2]
    elif list_var[0] == "/":
        return list_var[1] / list_var[2]
    elif list_var[0] == "+":
        return list_var[1] + list_var[2]
    else:
        return list_var[1] - list_var[2]

operator_list = ['+', '-', '*', '/']
assert x[0] in operator_list, 'Недопустимый оператор'

try:
    num1 = y[1]/y[2]
except ZeroDivisionError:
    print('На ноль делить нельзя')
except ValueError:
    print('Нельзя преобразовать в число')
    num1 = y[1]
    print(num1)
else:
    pass

print(calculate(y))

