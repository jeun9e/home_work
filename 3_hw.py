# Задача 1
def large(a,b):
    if a > b:
        print(a)
    elif b > a:
        print(b)
large(150,20)

# Задача 2

def Zad2(a,b):
    if abs(a-b) == 135:
        print('Yes')
    else:
         print('No')

Zad2(0,135)


# Задача 3
def zad3(month):
    if month == 12 or month == 1 or month == 2:
        print('Winter')
    if month == 3 or month == 4 or month == 5:
        print('Spring')
    if month in range (6,9):
        print('Summer')
    if month in range (9,12):
        print('Autumn')
zad3(9)


# Задача 4
def zad4(a,b,c):
    if a>10 and b>10 and c>10:
        print('Yes')
    else:
        print('No')
zad4(11,12,30)


#Задача 5
def zad5(a: list):
    rez = 0
    for i in a:
        if i > 0:
            rez = rez + 1
    return rez
print(zad5([1,-2,3,-4,5]))

# Задача 6

def zad6(a: int,b: int):
    return (a*12*29)+(b*29)
print(zad6(0,10))
