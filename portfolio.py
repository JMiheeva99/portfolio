def input_num(message: str) -> int:
    flag = True
    while(flag):
        try:
            num = int(input(message))
            flag = False
        except ValueError:
            print('Значение должно быть числом')
    return num

num_1 = input_num('Введите первое число : ')

ar = input('Введите арифметический знак(+,-,*,/) : ')

num_2 = input_num('Введите второе число : ')


if ar == '+':
    print('Результат сложения: ' + str(num_1 + num_2))
elif ar == '-':
    print('Результат вычитания: ' + str(num_1 - num_2))
elif ar == '*':
    print('Результат умножения: ' + str(num_1 * num_2))
elif ar == '/':
    try:
        print('Результат деления: ' + str(num_1 / num_2))
    except ZeroDivisionError:
        print('На 0 делить нельзя')
else:
    print('Арифметический знак не поддерживается в данном калькуляторе')