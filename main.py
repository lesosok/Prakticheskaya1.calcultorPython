import math

Procedure = 0
prodolzhit = 'да'

while prodolzhit == 'да':
    print('Выберите какую операцию вы хотите выполнить:')
    print('1. Сложить два числа')
    print('2. Вычесть первое из второго')
    print('3. Перемножить два числа')
    print('4. Разделить первое число на второе')
    print('5. Возвести в степень N первое число')
    print('6. Найти квадратный корень из числа')
    print('7. Найти факториал из числа')
    print('8. Найти синус')
    print('9. Найти косинус')
    print('10. Найти тангенс')

    try:
        Procedure = int(input())

    except:
        print('Введён неверный тип данных. Повторите попытку')

    if Procedure >= 11:
        print('Операции с таким номером нет. Повторите попытку')
    else:
        match Procedure:
            case 1:
                a = float(input('Введите первое число '))
                b = float(input('Введите второе число '))
                print('Результат: ', (a + b))

            case 2:
                a = float(input('Введите первое число '))
                b = float(input('Введите второе число '))
                print('Результат: ', (a - b))

            case 3:
                a = float(input('Введите первое число '))
                b = float(input('Введите второе число '))
                print('Результат: ', (a * b))

            case 4:
                a = float(input('Введите первое число '))
                b = float(input('Введите второе число '))
                if b == 0:
                    print('Нельзя делить на ноль! Повторите попытку')
                else:
                    print('Результат: ', (a / b))

            case 5:
                a = float(input('Введите первое число '))
                b = float(input('Введите степень, в которую нужно возвести первое число '))
                print('Результат: ', (a ** b))

            case 6:
                a = float(input('Введите число '))
                if a < 0:
                    print('Нельзя вычислить квадратный корень из отрицательного числа! Повторите попытку')
                else:
                    print('Результат: ', math.sqrt(a))

            case 7:
                a = int(input('Введите число '))
                if a < 0:
                    print('Нельзя вычислить факториал отрицательного числа! Повторите попытку')
                else:
                    print('Результат: ', math.factorial(a))

            case 8:
                a = float(input('Введите число '))
                print('Результат: ', math.sin(a))

            case 9:
                a = float(input('Введите число '))
                print('Результат: ', math.cos(a))

            case 10:
                a = float(input('Введите число '))
                print('Результат: ', math.tan(a))
    prodolzhit = input("Если хотите продолжить введите 'да' ")