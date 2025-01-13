# Задача 1 наибольшее число
def max_number(a,b):
    if a > b:
        print(a)
    elif b > a:
        print(b)
max_number(150,20)


# Задача 2 разница в 135
def task_2(a,b):
    if abs(a-b) == 135:
        print('Yes')
    else:
         print('No')

task_2(0,135)


# Задача 3 название сезона
def time_of_the_year(month):
    if month == 12 or month == 1 or month == 2:
        print('Winter')
    elif month == 3 or month == 4 or month == 5:
        print('Spring')
    elif month in range (6,9):
        print('Summer')
    elif month in range (9,12):
        print('Autumn')
time_of_the_year(9)


# Задача 4 числа больше 10
def more_ten(a,b,c):
    if a>10 and b>10 and c>10:
        print('Yes')
    else:
        print('No')
more_ten(11,12,30)


#Задача 5 количество положительных чисел
def positive_number(a: list):
    sum = 0
    for i in a:
        if i > 0:
            sum = sum + 1
    return sum
print(positive_number([1,-2,3,-4,5]))

# Задача 6 вывести количество дней
def sum_day(a: int,b: int):
    return (a*12*29)+(b*29)
print(sum_day(0,10))

