try:
    s = 0
    while True:
        print('Введите число (0 для окончания)')
        n = int(input())
        s = s + n
        if n == 0:
            print('Итоговая сумма: ' + str(s))
            break
        print('Текущая сумма: ' + str(s))
except ValueError:    
    print('Введите число')