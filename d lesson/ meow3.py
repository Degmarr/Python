meow = []
while True:
    print('Введите число (0 для окончания)')
    n = str(input())
    if n.isdigit() == True:
        if int(n) == 0:
            print('Отсортированный список' + str(sorted(meow,reverse=True)))
            break
        meow.append(n)
    elif n.isdigit() == False:
       print('Введите число')
