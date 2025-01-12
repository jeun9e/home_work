# Задача 1 наибольшее число
def large(a,b):
    if a > b:
        print(a)
    elif b > a:
        print(b)
large(150,20)


# Задача 2 разница в 135
def Zad2(a,b):
    if abs(a-b) == 135:
        print('Yes')
    else:
         print('No')

Zad2(0,135)


# Задача 3 название сезона
def zad3(month):
    if month == 12 or month == 1 or month == 2:
        print('Winter')
    elif month == 3 or month == 4 or month == 5:
        print('Spring')
    elif month in range (6,9):
        print('Summer')
    elif month in range (9,12):
        print('Autumn')
zad3(9)


# Задача 4 числа больше 10
def zad4(a,b,c):
    if a>10 and b>10 and c>10:
        print('Yes')
    else:
        print('No')
zad4(11,12,30)


#Задача 5 количество положительных чисел
def zad5(a: list):
    sum = 0
    for i in a:
        if i > 0:
            sum = sum + 1
    return sum
print(zad5([1,-2,3,-4,5]))

# Задача 6 вывести в количество дней
def zad6(a: int,b: int):
    return (a*12*29)+(b*29)
print(zad6(0,10))

