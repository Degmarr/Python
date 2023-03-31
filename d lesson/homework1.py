sales = [("14.04.2020", "Невероятные приключения Джоджо: Золотой ветер перемен, том №4", 44, 7440.0, 327360.0),
    ("19.01.2016", "Тетрадь Смерти, том №3", 51, 6590.0, 336090.0),
    ("21.08.2019", "Берсерк, том №5", 29, 8990.0, 260710.0),
    ("05.05.2022", "Великий из бродячих псов: Литературные гении, том №9", 75, 7990.0, 599250.0),
    ("31.01.2023", "Убить волка, том №2", 13, 11290, 146770.0),
    ("03.09.2022", "Человек-бензопила, том №1", 107, 6590.0, 705130.0),
    ("18.02.2019", "Хантер х Хантер, том №2", 60, 7490.0, 449400.0),
    ("02.03.2023", "Ванпанчмэн, том №17", 26, 6350.0, 165100.0),
    ("15.04.2022", "Благословение небожителей, том №5", 52, 8990.0, 467480.0),
    ("28.07.2017", "19 дней - Однажды, том №1", 34, 9900.0, 336600.0)]
print(sales[0], sales[1], sales[2], sales[3], sales[4], sales[5], sales[6], sales[7], sales[8], sales[9], sep = '\n')
def total_sales():
    s = sales[0][4] + sales[1][4] + sales[2][4] + sales[3][4] + sales[4][4] + sales[5][4] + sales[6][4] + sales[7][4] + sales[8][4] + sales[9][4]
    print('Общая сумма продаж: ', s)

total_sales()

def max_sales():
    for i in range(len(sales)):
        if max(sales[0][4], sales[1][4], sales[2][4], sales[3][4], sales[4][4], sales[5][4], sales[6][4], sales[7][4], sales[8][4], sales[9][4]) == sales[i][4]:
            print('Наибольшая сумма продажи: ', sales[i])

max_sales()            

def min_sales():
    for i in range(len(sales)):
        if min(sales[0][4], sales[1][4], sales[2][4], sales[3][4], sales[4][4], sales[5][4], sales[6][4], sales[7][4], sales[8][4], sales[9][4]) == sales[i][4]:
            print('Наименьшая сумма продажи: ', sales[i])

min_sales()  

def find_sale_by_data():
    d = input("Введите необходимую дату: ")
    for i in range(len(sales)):
        if d == sales[i][0]:
            print(sales[i])

find_sale_by_data()

l = int(input("Введите соответствующую цифру для выбора категории, по которой хотите рассортировать данные: дата(1), название(2), количество проданных единиц(3), цена за единицу(4) или общая сумма продажи(5) "))
if l == 1:
    a = (sales[0][0], sales[1][0], sales[2][0], sales[3][0], sales[4][0], sales[5][0], sales[6][0], sales[7][0], sales[8][0], sales[9][0])
    print("Сортировка по возрастанию ", sorted(a))
    print("Сортировка по убыванию ", sorted(a, reverse = True))
if l == 2:
    a = (sales[0][1], sales[1][1], sales[2][1], sales[3][1], sales[4][1], sales[5][1], sales[6][1], sales[7][1], sales[8][1], sales[9][1])
    print("Сортировка по возрастанию ", sorted(a))
    print("Сортировка по убыванию ", sorted(a, reverse = True))
if l == 3:
    a = (sales[0][2], sales[1][2], sales[2][2], sales[3][2], sales[4][2], sales[5][2], sales[6][2], sales[7][2], sales[8][2], sales[9][2])
    print("Сортировка по алфавиту ", sorted(a))
    print("Сортировка по алфавиту в обратном порядке ", sorted(a, reverse = True))
if l == 4:
    a = (sales[0][3], sales[1][3], sales[2][3], sales[3][3], sales[4][3], sales[5][3], sales[6][3], sales[7][3], sales[8][3], sales[9][3])
    print("Сортировка по возрастанию ", sorted(a))
    print("Сортировка по убыванию " + sorted(a, reverse = True))
if l == 5:
    a = (sales[0][4], sales[1][4], sales[2][4], sales[3][4], sales[4][4], sales[5][4], sales[6][4], sales[7][4], sales[8][4], sales[9][4])
    print("Сортировка по возрастанию ", sorted(a))
    print("Сортировка по убыванию ", sorted(a, reverse = True))